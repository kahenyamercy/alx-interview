#!/usr/bin/python3
"""Lockboxes challenge"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists):list of lists representing boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = set()  # Set to store visited boxes

    # Recursive function to explore boxes
    def dfs(box_index):
        visited.add(box_index)  # Mark the box as visited
        keys = boxes[box_index]  # Get keys in the current box
        for key in keys:
            if key not in visited and key < n:
                dfs(key)  # Explore the key

    dfs(0)  # Start DFS from the first box

    return len(visited) == n  # Check if all boxes are visited
