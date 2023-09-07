#!/usr/bin/python3

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def play_round(n):
    """Play one round of the Prime Game and return the winner's name."""
    nums = list(range(2, n+1))
    turn = 0  # 0 for Maria, 1 for Ben

    while True:
        found_prime = False
        for i in nums:
            if is_prime(i):
                found_prime = True
                multiples = list(range(i, n+1, i))
                nums = [x for x in nums if x not in multiples]
                break

        if not found_prime:
            return "Maria" if turn == 1 else "Ben"

        turn = 1 - turn  # switch turns

def isWinner(x, nums):
    """Determine the winner of x rounds of the Prime Game."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_round(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
