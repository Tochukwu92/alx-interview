#!/usr/bin/python3

'''prime game'''


def isWinner(x, nums):
    '''check who wins the game'''
    def sieve_of_eratosthenes(max_num):
        """
        Generate a list of primes up to max_num using
        the Sieve of Eratosthenes.
        """
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(max_num**0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, max_num + 1, i):
                    is_prime[multiple] = False
        return is_prime

    # Precompute prime information
    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    # Precompute prime counts up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    # Simulate the game for each n in nums
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
