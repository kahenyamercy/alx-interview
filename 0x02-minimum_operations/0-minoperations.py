#!/usr/bin/env python3
"""
Calculate fewest number of operations neededto result exactly n H characters"""


def minOperations(n):
    """
    Calculate fewest number of operations
    Args:
        n (int): The target number of H characters.

    Returns:
        int:fewest operations needed.If n impossible, return 0.
    """
    if n < 2:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
