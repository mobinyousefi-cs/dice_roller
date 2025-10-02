#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=========================================================================================================
Project: Dice Rolling Simulator (Tkinter + CLI)
File: gui.py
Author: Mobin Yousefi (GitHub: https://github.com/mobinyousefi-cs)
Created: 2025-10-02
Updated: 2025-10-02
License: MIT License (see LICENSE file for details)
=====================================================================================================

Description:
Tkinter-based GUI application that visualizes dice rolls with a simple spin animation, optional
seed for reproducibility, and support for rolling multiple dice and showing their sum.

Usage:
python -m dice_roller.main              # Launch GUI (default mode)
# or directly (not recommended; use the entrypoint above)
python -c "from dice_roller.gui import run_gui; run_gui()"

Notes:
- Cross-platform (Windows/macOS/Linux) using standard-library Tkinter.
- Large Unicode die face (⚀…⚅) + animated preview before showing results.
- GUI state (seed, #dice, sum mode) is independent from CLI usage.
"""



from __future__ import annotations

import time
import tkinter as tk
from tkinter import ttk
from typing import Optional

from .core import Dice, DiceRoller

DICE_UNICODE = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]


class DiceApp(tk.Tk):
    """
    Tkinter GUI for the Dice Rolling Simulator.

    Features:
    - Big dice face using Unicode symbols
    - "Roll" button with optional animation
    - Choice of number of dice and total/single mode
    - Seed input for reproducibility (optional)
    """

    def __init__(self) -> None:
        super().__init__()
        self.title("Dice Rolling Simulator — Mobin Yousefi")
        self.geometry("420x360")
        self.resizable(False, False)

        # State
        self._seed_var = tk.StringVar()
        self._count_var = tk.IntVar(value=1)
        self._sum_mode_var = tk.BooleanVar(value=False)
        self._result_var = tk.StringVar(value="—")
        self._status_var = tk.StringVar(value="Ready")

        # Layout
        self._build_ui()

        # Roller initialized lazily based on seed
        self.roller: Optional[DiceRoller] = None

    def _build_ui(self) -> None:
        container = ttk.Frame(self, padding=16)
        container.pack(fill="both", expand=True)

        title = ttk.Label(container, text="Dice Rolling Simulator", font=("Segoe UI", 16, "bold"))
        title.pack(pady=(0, 10))

        # Dice face display
        self.face_label = ttk.Label(container, text="⚀", font=("Segoe UI Symbol", 72))
        self.face_label.pack(pady=4)

        # Controls
        controls = ttk.Frame(container)
        controls.pack(pady=8, fill="x")

        ttk.Label(controls, text="Seed (optional):").grid(row=0, column=0, sticky="w")
        ttk.Entry(controls, textvariable=self._seed_var, width=12).grid(row=0, column=1, padx=6)

        ttk.Label(controls, text="# of dice:").grid(row=0, column=2, sticky="e")
        ttk.Spinbox(controls, from_=1, to=12, textvariable=self._count_var, width=6).grid(
            row=0, column=3, padx=6
        )

        ttk.Checkbutton(controls, text="Show sum", variable=self._sum_mode_var).grid(
            row=0, column=4, padx=6
        )

        # Roll button
        ttk.Button(container, text="Roll 🎲", command=self.on_roll).pack(pady=8)

        # Result
        result_row = ttk.Frame(container)
        result_row.pack(pady=8)
        ttk.Label(result_row, text="Result:", font=("Segoe UI", 10, "bold")).pack(side="left", padx=(0, 6))
        ttk.Label(result_row, textvariable=self._result_var, font=("Segoe UI", 12)).pack(side="left")

        # Status bar
        ttk.Separator(container).pack(fill="x", pady=(14, 6))
        status = ttk.Label(container, textvariable=self._status_var, anchor="w")
        status.pack(fill="x")

        for child in container.winfo_children():
            if isinstance(child, ttk.Frame):
                for grand in child.winfo_children():
                    grand.grid_configure(pady=2)

    def _ensure_roller(self) -> None:
        seed_text = self._seed_var.get().strip()
        seed_val = None
        if seed_text:
            try:
                seed_val = int(seed_text)
            except ValueError:
                # Simple hash fallback for string seeds
                seed_val = abs(hash(seed_text)) % (2**31)
        self.roller = DiceRoller(Dice(sides=6, faces=DICE_UNICODE, values=[1, 2, 3, 4, 5, 6]), seed=seed_val)

    def animate_roll(self, frames: int = 10, delay_ms: int = 30) -> None:
        # Simple spin animation to mimic rolling
        for i in range(frames):
            self.face_label.config(text=DICE_UNICODE[i % 6])
            self.update_idletasks()
            time.sleep(delay_ms / 1000.0)

    def on_roll(self) -> None:
        if self.roller is None:
            self._ensure_roller()
        assert self.roller is not None

        n = max(1, int(self._count_var.get()))
        sum_mode = bool(self._sum_mode_var.get())

        self._status_var.set("Rolling…")
        self.animate_roll()

        results = self.roller.roll(n)

        # Update face with last die to keep it intuitive
        last_face = DICE_UNICODE[results[-1] - 1]
        self.face_label.config(text=last_face)

        if sum_mode and n > 1:
            self._result_var.set(f"{' + '.join(map(str, results))} = {sum(results)}")
        elif n == 1:
            self._result_var.set(str(results[0]))
        else:
            self._result_var.set(", ".join(map(str, results)))

        self._status_var.set("Ready")


def run_gui() -> None:
    app = DiceApp()
    app.mainloop()
