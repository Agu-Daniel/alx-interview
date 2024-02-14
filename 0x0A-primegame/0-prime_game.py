#!/usr/bin/python3
"""Maria and Ben are playing a game"""


def isWinner(x, nums):
    """x - number of rounds
    nums - numbers of list
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben_var = 0
    maria_var = 0

    b = [1 for x in range(sorted(nums)[-1] + 1)]
    b[0], b[1] = 0, 0
    for i in range(2, len(b)):
        remove_multiples(b, i)

    for i in nums:
        if sum(b[0:i + 1]) % 2 == 0:
            ben_var += 1
        else:
            maria_var += 1
    if ben_var > maria_var:
        return "Ben"
    if maria_var > ben_var:
        return "Maria"
    return None



def remove_multiples(ls, x):
    """removes multiple of primes
    """
    for j in range(2, len(ls)):
        try:
            ls[j * x] = 0
        except (ValueError, IndexError):
            break