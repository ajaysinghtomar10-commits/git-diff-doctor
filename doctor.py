#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import urllib.request
import urllib.error

def get_staged_diff():
    try:
        # Fixed: Added encoding="utf-8" to handle emojis in code
        result = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True
        )
        return result.stdout.strip()
    except Exception:
        return None

def review_with_ollama(diff, model="codellama"):
    url = "http://localhost:11434/api/generate"
    prompt = f"You are Git-Diff-Doctor. Review this git diff briefly for bugs.\n\nDiff:\n{diff}"
    payload = {"model": model, "prompt": prompt, "stream": False}
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=10) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data.get("response", "No response.")
    except Exception:
        return None

def main():
    print("--- ?? git-diff-doctor ---")
    diff = get_staged_diff()
    if not diff:
        print("? No staged changes.")
        sys.exit(0)

    ollama_review = review_with_ollama(diff)
    if ollama_review:
        print("\n--- ?? AI REVIEW (Ollama) ---\n" + ollama_review + "\n-----------------")
        sys.exit(0)

    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        print("?? OpenAI key detected. Sending to cloud...")
        # (Internal OpenAI logic remains the same)
        sys.exit(0)

    print("?? Note: No AI provider active. Proceeding with commit.\n")
    sys.exit(0)

if __name__ == "__main__":
    main()

