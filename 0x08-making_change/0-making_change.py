#!/usr/bin/python3
"""
Given a pile of coins of different values,
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total amount.

    Args:
    coins (list of int): List of coin values available.
    total (int): Target total amount.

    Returns:
    int: Fewest number of coins needed to meet the total.
         Returns -1 if the total cannot be met by any combination of coins.

    Raises:
    ValueError: If total is less than or equal to 0.

    Note:
    - The function assumes an infinite number of each
    denomination of coin in the list.
    - The value of a coin will always be an integer greater than 0.
    - The solution's runtime will be evaluated in this task.
    """
    if total <= 0:
        return 0

    if total == 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    # Initialize variables
    num_coins = 0
    remainder = total

    # Greedy algorithm to find the minimum number of coins
    for coin in coins:
        if remainder >= coin:
            num_coins += remainder // coin
            remainder %= coin

    if remainder == 0:
        return num_coins
    else:
        return -1
