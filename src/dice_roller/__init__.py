#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: __init__.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Package initializer exporting public API:
- Dice, DiceRoller (core logic)
- run_gui (Tkinter launcher)
- main (CLI/GUI entrypoint)

Usage:
from dice_roller import Dice, DiceRoller, run_gui, main
"""



"""
Dice Roller package.

Provides:
- `Dice`: a fair (or custom) N-sided die
- `DiceRoller`: utility for rolling dice with optional animation delays
- `run_gui()`: start the Tkinter GUI
- `main()`: CLI entry point
"""

from .core import Dice, DiceRoller
from .gui import run_gui
from .main import main

__all__ = ["Dice", "DiceRoller", "run_gui", "main"]
__version__ = "0.1.0"
