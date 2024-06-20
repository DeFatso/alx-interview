#!/usr/bin/python3
"""
Main file for testing
"""


def makeChange(coins, total):
    """
        make change
    """
    if total <= 0:
        return 0

    """
    Initialize the dp array with total+1 (a value greater than
    any possible number of coins)
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] <= total else -1
