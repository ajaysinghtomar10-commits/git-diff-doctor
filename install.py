import os
import stat
import shutil
import sys

def install():
    hook_path = os.path.join(".git", "hooks", "pre-commit")
    
    if not os.path.exists(".git"):
        print("? Error: Not a git repository. Run this inside your project root.")
        return

    # The command that will be placed inside the git hook
    # It tells Git to run our python doctor script before every commit
    hook_content = "#!/bin/sh\npython doctor.py\n"

    try:
        with open(hook_path, "w") as f:
            f.write(hook_content)
        
        # Make the file executable (important for Mac/Linux users who clone your repo)
        st = os.stat(hook_path)
        os.chmod(hook_path, st.st_mode | stat.S_IEXEC)
        
        print("? git-diff-doctor installed successfully!")
        print("The doctor will now automatically screen your code before every commit.")
    except Exception as e:
        print(f"? Installation failed: {e}")

if __name__ == "__main__":
    install()

