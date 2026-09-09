#!/usr/bin/env python3
"""
git-diff-doctor - Zero-dependency AI Pre-commit Reviewer
Maintainer: Ajay Singh Tomar
"""

import subprocess
import sys

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
    except subprocess.CalledProcessError as e:
        print(f" Error executing git diff: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(" Git is not installed or not in PATH.")
        sys.exit(1)

def main():
    print(" git-diff-doctor is inspecting your staged changes...\n")
    diff = get_staged_diff()

    if not diff:
        print(" No staged changes found. Nothing to review.")
        print(" Tip: Use 'git add <file>' to stage files before running git-diff-doctor.")
        return

    print(f" Found staged changes ({len(diff)} characters).\n")
    print("--- STAGED DIFF PREVIEW ---")
    preview = diff[:500] + "\n...[truncated]" if len(diff) > 500 else diff
    print(preview)
    print("---------------------------")

if __name__ == "__main__":
    main()

