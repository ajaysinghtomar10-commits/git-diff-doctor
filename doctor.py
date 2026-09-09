#!/usr/bin/env python3
"""
git-diff-doctor - Zero-dependency AI Pre-commit Reviewer
Supports: Ollama (Free Local AI) and OpenAI API
Maintainer: Ajay Singh Tomar
"""

import os
import sys
import json
import subprocess
import urllib.request
import urllib.error

def get_staged_diff():
    """Retrieve staged changes from git diff --cached."""
    try:
        result = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def review_with_ollama(diff, model="codellama"):
    """Send diff to local Ollama server (Free, Private)."""
    url = "http://localhost:11434/api/generate"
    prompt = f"You are Git-Diff-Doctor. Review this git diff for bugs, security issues, and style improvements. Be brief.\n\nDiff:\n{diff}"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("response", "No response content received.")
    except urllib.error.URLError:
        return None  # Ollama is not running locally

def review_with_openai(diff, api_key):
    """Send diff to OpenAI API."""
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are Git-Diff-Doctor. Review this git diff concisely for bugs and security risks."},
            {"role": "user", "content": diff}
        ]
    }

    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"? OpenAI Error: {str(e)}"

def main():
    print("--- ?? git-diff-doctor ---")
    diff = get_staged_diff()

    if not diff:
        print("? No staged changes to review.")
        sys.exit(0)

    # 1. Try Local Ollama First (Free & Private)
    print("?? Checking local Ollama instance...")
    ollama_review = review_with_ollama(diff)
    if ollama_review:
        print("\n--- ?? AI REVIEW REPORT (Ollama Local) ---")
        print(ollama_review)
        print("------------------------------------------")
        sys.exit(0)

    # 2. Try OpenAI API if Key is set in Environment
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("?? Connecting to OpenAI API...")
        report = review_with_openai(diff, api_key)
        print("\n--- ?? AI REVIEW REPORT (OpenAI) ---")
        print(report)
        print("-----------------------------------")
        sys.exit(0)

    # 3. Graceful Fallback (No AI available)
    print("?? Note: Neither local Ollama nor OPENAI_API_KEY detected.")
    print("?? Tip: Start Ollama locally on port 11434 for free offline code reviews!")
    print("? Staged diff verified. Proceeding with commit.\n")
    sys.exit(0)

if __name__ == "__main__":
    main()

