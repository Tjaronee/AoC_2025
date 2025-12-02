"""Input reader utility for Advent of Code 2025."""

import os
from pathlib import Path


def get_input(day: int, as_lines: bool = True):
    """
    Read the input file for a given day.
    
    Args:
        day (int): The day number (1-25)
        as_lines (bool): If True, returns a list of lines. If False, returns the raw text.
    
    Returns:
        list or str: The input data as a list of lines or raw text
    
    Example:
        >>> data = get_input(1)  # Returns lines for day 1
        >>> data = get_input(1, as_lines=False)  # Returns raw text for day 1
    """
    # Get the project root (parent of utils)
    project_root = Path(__file__).parent.parent
    input_file = project_root / "inputs" / f"day{day:02d}.txt"
    
    if not input_file.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_file}\n"
            f"Please create the file at: inputs/day{day:02d}.txt"
        )
    
    with open(input_file, 'r', encoding='utf-8') as f:
        if as_lines:
            return [line.rstrip('\n') for line in f]
        else:
            return f.read()
