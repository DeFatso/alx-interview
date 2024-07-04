#!/usr/bin/python3

def isWinner(x, nums):
    """ Determine the winner of each game round between Maria and Ben. """

    if not nums or x <= 0:
        return None

    max_num = max(nums)

    # Sieve of Eratosthenes to determine prime numbers up to max_num
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1

    # Create a list to count the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1]
        if is_prime[i]:
            prime_count[i] += 1

    maria = 0
    ben = 0
    for num in nums:
        if prime_count[num] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
