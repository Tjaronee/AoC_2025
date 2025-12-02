"""Tests for parsing utilities."""

import pytest
from aoc_utils import parse_ints, parse_grid, parse_blocks, neighbors_4, neighbors_8


def test_parse_ints():
    """Test integer extraction from strings."""
    assert parse_ints("x=5, y=-3, z=100") == [5, -3, 100]
    assert parse_ints("no numbers here") == []
    assert parse_ints("123") == [123]


def test_parse_grid():
    """Test grid parsing."""
    grid = parse_grid(['#.', '.#'])
    assert grid == {(0, 0): '#', (0, 1): '.', (1, 0): '.', (1, 1): '#'}
    
    grid = parse_grid(['abc'])
    assert grid == {(0, 0): 'a', (0, 1): 'b', (0, 2): 'c'}


def test_parse_blocks():
    """Test block separation."""
    result = parse_blocks(['a', 'b', '', 'c', 'd'])
    assert result == [['a', 'b'], ['c', 'd']]
    
    result = parse_blocks(['a', '', 'b'])
    assert result == [['a'], ['b']]
    
    result = parse_blocks(['a', 'b'])
    assert result == [['a', 'b']]


def test_neighbors_4():
    """Test 4-directional neighbors."""
    neighbors = neighbors_4(5, 5)
    assert len(neighbors) == 4
    assert (4, 5) in neighbors  # up
    assert (6, 5) in neighbors  # down
    assert (5, 4) in neighbors  # left
    assert (5, 6) in neighbors  # right


def test_neighbors_8():
    """Test 8-directional neighbors."""
    neighbors = neighbors_8(5, 5)
    assert len(neighbors) == 8
    assert (4, 4) in neighbors  # diagonal
    assert (6, 6) in neighbors  # diagonal
