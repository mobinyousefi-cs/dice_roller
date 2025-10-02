#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: core.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Core, framework-agnostic logic for rolling N-sided dice. Exposes `Dice` (a configurable die with
custom faces/values) and `DiceRoller` (seedable utility for deterministic or random rolls).

Usage:
# As a library:
from dice_roller.core import Dice, DiceRoller
roller = DiceRoller(seed=42); print(roller.roll(3)); print(roller.roll_sum(2))

Notes:
- Pure-Python, no GUI/IO. Safe to unit test.
- Unicode faces (⚀…⚅) supported via the `faces` argument.
- Determinism via `seed` (uses `random.Random`).
"""



from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence


@dataclass(frozen=True)
class Dice:
    """
    A simple N-sided die. By default uses faces 1..N with equal probability.

    You can also pass explicit `faces` (e.g., ["⚀","⚁","⚂","⚃","⚄","⚅"]) to
    customize the appearance; the logical value returned by `roll()` is the
    index (1-based) of the selected face unless `values` is provided.
    """

    sides: int = 6
    faces: Optional[Sequence[str]] = None
    values: Optional[Sequence[int]] = None

    def __post_init__(self) -> None:
        if self.sides < 2:
            raise ValueError("A die must have at least 2 sides.")
        if self.faces is not None and len(self.faces) != self.sides:
            raise ValueError("faces length must match `sides`.")
        if self.values is not None and len(self.values) != self.sides:
            raise ValueError("values length must match `sides`.")

    def face_for(self, idx: int) -> str:
        if self.faces:
            return self.faces[idx]
        # Default: use the integer as string
        return str(idx + 1)

    def value_for(self, idx: int) -> int:
        if self.values:
            return self.values[idx]
        # Default: index (0..N-1) -> 1..N
        return idx + 1

    def roll_index(self, rng: random.Random) -> int:
        return rng.randrange(self.sides)

    def roll(self, rng: Optional[random.Random] = None) -> int:
        """Return the numeric value of a single roll."""
        rng = rng or random
        idx = self.roll_index(rng)
        return self.value_for(idx)


class DiceRoller:
    """
    Utility to roll one or more dice with an optional seed for reproducibility.
    """

    def __init__(self, dice: Dice | None = None, seed: int | None = None) -> None:
        self.dice = dice or Dice(
            sides=6,
            faces=["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"],
            values=[1, 2, 3, 4, 5, 6],
        )
        self.rng = random.Random(seed)

    def roll(self, times: int = 1) -> List[int]:
        if times < 1:
            raise ValueError("times must be >= 1")
        return [self.dice.roll(self.rng) for _ in range(times)]

    def roll_sum(self, times: int = 2) -> int:
        return sum(self.roll(times))

    def roll_sequence(self, sequence: Iterable[int]) -> List[int]:
        # Convenience when callers want variable batch sizes (validated for >=1)
        return [self.roll(t)[0] if t == 1 else sum(self.roll(t)) for t in sequence]
