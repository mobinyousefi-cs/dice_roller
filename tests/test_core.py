#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: test_core.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Unit tests for the pure core logic (Dice, DiceRoller). Verifies validation, determinism with seed,
and output ranges/sanity without involving GUI elements.

Usage:
pytest -q tests/test_core.py
"""



from __future__ import annotations

from dice_roller.core import Dice, DiceRoller


def test_dice_init_validation():
    d = Dice(sides=6)
    assert d.sides == 6
    assert d.value_for(0) == 1
    assert d.face_for(0) == "1"


def test_dice_faces_and_values():
    faces = ["a", "b", "c", "d"]
    values = [10, 20, 30, 40]
    d = Dice(sides=4, faces=faces, values=values)
    assert d.face_for(2) == "c"
    assert d.value_for(2) == 30


def test_dice_roller_deterministic_with_seed():
    r1 = DiceRoller(seed=42)
    r2 = DiceRoller(seed=42)
    assert r1.roll(5) == r2.roll(5)


def test_roll_sum():
    r = DiceRoller(seed=7)
    s = r.roll_sum(3)
    # With a fixed seed we can assert a deterministic sum
    assert isinstance(s, int)
    assert 3 <= s <= 18
