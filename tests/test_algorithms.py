"""Tests for algorithm utilities."""

import pytest
from aoc_utils import bfs, dijkstra, flood_fill


def test_bfs_simple():
    """Test BFS on a simple graph."""
    # Graph: 0 -> 1 -> 2 -> 3
    def get_neighbors(node):
        return [node + 1] if node < 3 else []
    
    path = bfs(0, get_neighbors, lambda x: x == 3)
    assert path == [0, 1, 2, 3]


def test_bfs_no_path():
    """Test BFS when no path exists."""
    def get_neighbors(node):
        return [node + 1] if node < 2 else []
    
    path = bfs(0, get_neighbors, lambda x: x == 5)
    assert path is None


def test_flood_fill():
    """Test flood fill."""
    # Simple 3x3 grid, all connected
    def get_neighbors(pos):
        r, c = pos
        neighbors = []
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                neighbors.append((nr, nc))
        return neighbors
    
    result = flood_fill((0, 0), get_neighbors)
    assert len(result) == 9  # All 9 cells in 3x3 grid
