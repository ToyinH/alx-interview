#!/usr/bin/python3
"""
Prime Game
"""

def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime statuses for numbers up to max_n using the Sieve of Eratosthenes
    """
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

def count_primes_up_to(is_prime, max_n):
    """
    Count the number of primes up to each number from 0 to max_n
    """
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)
    return prime_count

def isWinner(x, nums):
    """
    Determine the winner after x rounds
    """
    if x <= 0 or not nums:
        return None
    
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)
    prime_count = count_primes_up_to(is_prime, max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 0:
            continue
        
        # Use precomputed prime counts
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
