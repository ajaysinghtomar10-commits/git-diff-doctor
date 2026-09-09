# 🩺 git-diff-doctor

> A zero-dependency, provider-agnostic Git hook tool that performs local AI code reviews before commits hit remote repositories.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## 🚀 Key Features

- ⚡ **Zero External Dependencies:** Built 100% with Python standard libraries (`urllib`, `subprocess`, `json`).
- 🦙 **Free Local AI Support:** Auto-detects local [Ollama](https://ollama.com) instances (`codellama`, `llama3`).
- 🌐 **Cloud AI Support:** Works with OpenAI (`OPENAI_API_KEY`).
- 🛡️ **Privacy First:** Your code stays local when using Ollama.
- ⚡ **One-Command Install:** Auto-injects into `.git/hooks/pre-commit`.

## 🛠️ Quick Setup

1. Copy `doctor.py` and `install.py` into your repository.
2. Run the installer:
   python install.py
3. Commit code as usual:
   git add .
   git commit -m "my commit"

*The doctor will automatically inspect your staged changes before finalizing the commit!*

## 📄 License

MIT © [Ajay Singh Tomar](https://github.com/ajaysinghtomar10-commits)