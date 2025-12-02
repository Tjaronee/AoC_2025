"""Tests for input utilities."""

import pytest
from pathlib import Path
from aoc_utils import getInput


def test_getInput_returns_list():
    """Test that getInput returns a list."""
    result = getInput(1)
    assert isinstance(result, list)


def test_getInput_returns_strings():
    """Test that getInput returns a list of strings."""
    result = getInput(1)
    assert all(isinstance(line, str) for line in result)
