# Dice Rolling Simulator (Tkinter + CLI)

A clean, testable Dice Rolling Simulator written in Python, featuring:

- 🎲 **GUI** built with Tkinter (fast, cross-platform)
- 🧪 **Unit tests** for the core logic (pytest)
- 🧰 **CLI** mode for quick rolls or scripting
- 🧼 **Quality**: Ruff lint + Black formatting + GitHub Actions CI
- 📦 Modern packaging with `pyproject.toml` (PEP 621)

## Quick Start

```bash
# 1) Create & activate a venv (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install (dev)
pip install -e .[dev]

# 3) Run GUI
dice-roller

# 4) Run CLI
dice-roller --cli -n 3 --sum --seed 123
