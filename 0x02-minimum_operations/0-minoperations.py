#!/usr/bin/python3
"""Minimum operations"""


def minOperations(target_h):
    """Minimum operations"""
    if target_h == 1:
        return 0

    # Initialize a list to keep track of the minimum operations for each step
    min_operations = [0] * (target_h + 1)

    # Iterate through each step of the puzzle
    for current_h in range(2, target_h + 1):
        # Assume the maximum possible operations initially
        min_operations[current_h] = current_h

        # Try different ways to break down the current step into smaller steps
        for divisor in range(2, int(current_h ** 0.5) + 1):
            if current_h % divisor == 0:
                # Update the minimum operations if we find a better way
                min_operations[current_h] = min(
                    min_operations[current_h],
                    min_operations[divisor] + current_h // divisor,
                    min_operations[current_h // divisor] + divisor
                )

    # Return the minimum operations needed for the target number of "H"s
    return min_operations[target_h]
