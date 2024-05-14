#!/usr/bin/python3
""" Prime Game """


def is_prime(num):
    """
    Check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determine the winner of the game.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [num for num in range(2, n+1) if is_prime(num)]
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
