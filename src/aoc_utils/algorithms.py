"""Algorithm utilities for Advent of Code problems."""

from typing import List, Callable, TypeVar, Set, Dict, Tuple, Optional
from collections import deque
import heapq

T = TypeVar('T')


def bfs(start: T, get_neighbors: Callable[[T], List[T]], 
        is_goal: Callable[[T], bool]) -> Optional[List[T]]:
    """Breadth-first search to find shortest path.
    
    Args:
        start: Starting state
        get_neighbors: Function that returns neighbors of a state
        is_goal: Function that returns True if state is the goal
        
    Returns:
        List representing path from start to goal, or None if no path exists
    """
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        if is_goal(current):
            return path
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None


def dijkstra(start: T, get_neighbors: Callable[[T], List[Tuple[T, int]]], 
             is_goal: Callable[[T], bool]) -> Optional[Tuple[int, List[T]]]:
    """Dijkstra's algorithm to find shortest weighted path.
    
    Args:
        start: Starting state
        get_neighbors: Function returning list of (neighbor, cost) tuples
        is_goal: Function that returns True if state is the goal
        
    Returns:
        Tuple of (total_cost, path) or None if no path exists
    """
    heap = [(0, start, [start])]
    visited = set()
    
    while heap:
        cost, current, path = heapq.heappop(heap)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if is_goal(current):
            return (cost, path)
        
        for neighbor, edge_cost in get_neighbors(current):
            if neighbor not in visited:
                heapq.heappush(heap, (cost + edge_cost, neighbor, path + [neighbor]))
    
    return None


def flood_fill(start: T, get_neighbors: Callable[[T], List[T]]) -> Set[T]:
    """Find all reachable positions from start using flood fill.
    
    Args:
        start: Starting position
        get_neighbors: Function that returns valid neighbors
        
    Returns:
        Set of all reachable positions
    """
    visited = {start}
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited
