"""Parsing utilities for Advent of Code problems."""

from typing import List, Tuple, Dict, Any
import re


def parse_ints(text: str) -> List[int]:
    """Extract all integers from a string.
    
    Args:
        text: String containing integers
        
    Returns:
        List of integers found in the text
        
    Example:
        >>> parse_ints("x=5, y=-3, z=100")
        [5, -3, 100]
    """
    return [int(x) for x in re.findall(r'-?\d+', text)]


def parse_grid(lines: List[str]) -> Dict[Tuple[int, int], str]:
    """Convert list of strings into a coordinate dictionary.
    
    Args:
        lines: List of strings representing rows of a grid
        
    Returns:
        Dictionary mapping (row, col) coordinates to characters
        
    Example:
        >>> parse_grid(['#.', '.#'])
        {(0, 0): '#', (0, 1): '.', (1, 0): '.', (1, 1): '#'}
    """
    grid = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            grid[(row, col)] = char
    return grid


def parse_blocks(lines: List[str]) -> List[List[str]]:
    """Split input into blocks separated by empty lines.
    
    Args:
        lines: List of strings
        
    Returns:
        List of blocks, where each block is a list of strings
        
    Example:
        >>> parse_blocks(['a', 'b', '', 'c', 'd'])
        [['a', 'b'], ['c', 'd']]
    """
    blocks = []
    current_block = []
    
    for line in lines:
        if line.strip() == '':
            if current_block:
                blocks.append(current_block)
                current_block = []
        else:
            current_block.append(line)
    
    if current_block:
        blocks.append(current_block)
    
    return blocks


def neighbors_4(row: int, col: int) -> List[Tuple[int, int]]:
    """Get 4 orthogonal neighbors (up, down, left, right).
    
    Args:
        row: Row coordinate
        col: Column coordinate
        
    Returns:
        List of (row, col) tuples for adjacent positions
    """
    return [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]


def neighbors_8(row: int, col: int) -> List[Tuple[int, int]]:
    """Get 8 neighbors including diagonals.
    
    Args:
        row: Row coordinate
        col: Column coordinate
        
    Returns:
        List of (row, col) tuples for all adjacent positions
    """
    neighbors = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            neighbors.append((row + dr, col + dc))
    return neighbors
