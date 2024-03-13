#!/usr/bin/python3
#lockboxes
def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        visited.add(current_box)

        # Push all keys from the current box onto the stack
        for key in boxes[current_box]:
            if key < n and key not in visited:
                stack.append(key)

    # Check if all boxes are visited
    return len(visited) == n
