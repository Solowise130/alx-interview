#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create an array to store results of subproblems
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Fill dp[] in a bottom-up manner
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If total cannot be made up by any combination of the coins
    if dp[total] == float('inf'):
        return -1

    return dp[total]
