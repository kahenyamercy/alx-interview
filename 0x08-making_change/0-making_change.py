#!/usr/bin/python3
"""making change"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total amount
    dp = [float('inf')] * (total + 1)

    # Base case: 0 coins are needed for total = 0
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each total amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total amount is not reachable, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]