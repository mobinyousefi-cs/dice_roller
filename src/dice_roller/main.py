#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: main.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Unified entrypoint for the Dice Rolling Simulator. Runs the Tkinter GUI by default, or a lightweight
CLI when `--cli` is passed. The CLI supports multiple dice, summation, and a reproducible seed.

Usage:
# GUI (default):
python -m dice_roller.main

# CLI:
python -m dice_roller.main --cli [-n NUM] [--sum] [--seed SEED]
# Examples:
python -m dice_roller.main --cli
python -m dice_roller.main --cli -n 3 --sum --seed 123

Notes:
- Exposes `parse_args(argv)` for testing and `main(argv)` for programmatic invocation.
- Exit codes: 0 on success; non-zero reserved for future error cases.
"""



from __future__ import annotations

import argparse
import sys
from typing import List

from .core import DiceRoller
from .gui import run_gui


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Dice Rolling Simulator — GUI & CLI",
        prog="dice-roller",
    )
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode (no GUI).")
    parser.add_argument("-n", "--num", type=int, default=1, help="Number of dice to roll (CLI).")
    parser.add_argument("--sum", dest="sum_mode", action="store_true", help="Print the sum (CLI).")
    parser.add_argument("--seed", type=int, default=None, help="Seed for reproducibility (CLI).")
    return parser.parse_args(argv)


def _cli_main(ns: argparse.Namespace) -> int:
    roller = DiceRoller(seed=ns.seed)
    results = roller.roll(ns.num)
    if ns.sum_mode and ns.num > 1:
        print(f"Results: {results}  -> Sum = {sum(results)}")
    else:
        print(results if ns.num > 1 else results[0])
    return 0


def main(argv: List[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    ns = parse_args(argv)
    if ns.cli:
        return _cli_main(ns)
    run_gui()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
