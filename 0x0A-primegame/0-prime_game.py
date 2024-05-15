#!/usr/bin/python3
"""
Prime Game
"""


def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum(1 for i in range(1, n+1) if is_prime(i))
        # If the count of prime numbers is even, Ben wins, otherwise Maria wins
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
