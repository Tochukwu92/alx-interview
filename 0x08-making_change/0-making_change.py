#!/usr/bin/python3

'''Making change module'''


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.
    :param coins: List of integers representing the values of the coins.
    :param total: Integer representing the total amount.
    :return: Fewest number of coins needed or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)

    # Initialize the dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case

    # Fill the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
