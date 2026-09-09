# ?? git-diff-doctor

> A zero-dependency, provider-agnostic Git hook tool that acts as a local code reviewer before commits hit remote repositories.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

`git-diff-doctor` intercepts your staged Git changes (`git diff --cached`) and runs a lightweight diagnostic check using local or cloud AI providers (Ollama, OpenAI, Anthropic) before allowing the commit to proceed.

## ?? Key Features

- ? **Zero External Dependencies:** Built strictly with Python standard library modules.
- ?? **Provider Agnostic:** Connect to Ollama (free local AI), OpenAI, or Anthropic.
- ??? **Silent & Private:** Inspects staged code locally—no code leaves your workspace unless routed to your chosen provider.
- ?? **Pre-Commit Hook Ready:** Easily drops into `.git/hooks/pre-commit`.

## ??? Installation & Usage

*(Work in progress — Active initial development)*

## ?? License

MIT © [Ajay Singh Tomar](https://github.com/ajaysinghtomar10-commits)
