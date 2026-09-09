#!/usr/bin/env python3
import subprocess
import sys
import json
import urllib.request

def get_staged_diff():
    try:
        result = subprocess.run(["git", "diff", "--cached"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return None

def review_code(diff, api_key, provider="openai"):
    """Sends the diff to AI for review using pure Python (urllib)."""
    
    # The instructions for the AI "Doctor"
    system_prompt = "You are Git-Diff-Doctor. Review this code diff for bugs, security risks, and style. Be concise."
    
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": "gpt-4o", # You can change this to gpt-3.5-turbo
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Review this git diff:\n\n{diff}"}
        ]
    }

    print("?? Doctor is analyzing the code... Please wait.")
    
    try:
        req = urllib.request.Request(url, data=json.dumps(data).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            return res_data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"? Error connecting to AI: {str(e)}"

def main():
    print("--- ?? git-diff-doctor ---")
    diff = get_staged_diff()

    if not diff:
        print("? No staged changes to review.")
        return

    # For now, we ask for a key. Later we will use a config file.
    print("Tip: To use OpenAI, you need an API Key. (Enter to skip/dummy test)")
    key = input("Enter OpenAI API Key: ").strip()

    if not key:
        print("\nSkipping AI review (No API Key provided).")
        print("Diff found successfully. The engine is ready!")
    else:
        report = review_code(diff, key)
        print("\n--- ?? AI REVIEW REPORT ---")
        print(report)
        print("--------------------------")

if __name__ == "__main__":
    main()

