#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: test_main.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Argument parsing tests for the CLI/GUI entrypoint. Ensures default flags, types, and values are parsed
as expected.

Usage:
pytest -q tests/test_main.py
"""



from __future__ import annotations

from dice_roller.main import parse_args


def test_parse_args_defaults():
    ns = parse_args([])
    assert not ns.cli
    assert ns.num == 1
    assert ns.sum_mode is False
    assert ns.seed is None


def test_parse_args_cli_flags():
    ns = parse_args(["--cli", "-n", "3", "--sum", "--seed", "123"])
    assert ns.cli
    assert ns.num == 3
    assert ns.sum_mode
    assert ns.seed == 123
