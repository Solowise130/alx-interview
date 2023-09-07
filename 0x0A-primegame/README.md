Prime Game

Description:

Maria and Ben are engaged in an enthralling game that tests knowledge of prime numbers and strategic thinking. Here's how the game works:

Rules:

Initialization: The game starts with a set of consecutive integers from 1 up to and including 
�
n.

Prime Picking: Players alternate turns, beginning with Maria, to select a prime number from the current set.

Elimination: Once a prime number is chosen, that number and all its multiples are eradicated from the set.

Objective: During their turn, each player's main goal is to pick a prime number. If a player cannot select a prime number when it's their turn, they lose that round.

Rounds: The players contest in 
�
x rounds, and each round might have a different value of 
�
n. The overall victor is the player who triumphs in the most rounds.

Objective:

Design a function to simulate this game and determine who the winner is, given the number of rounds and the list of values of 
�
n for each round.

Function Prototype:

def isWinner(x: int, nums: List[int]) -> str:
    pass


Constraints:
�
x and 
�
n will not exceed 10,000.
No external packages are allowed.
Example:
For 
�
=
3
x=3 and 
�
�
�
�
=
[
4
,
5
,
1
]
nums=[4,5,1]:

First Round with 
�
=
4
n=4: Ben wins.
Second Round with 
�
=
5
n=5: Maria wins.
Third Round with 
�
=
1
n=1: Ben wins.
Result: Ben wins the most rounds.

Usage:

$ python main.py
Winner: Ben

