Making Change

"Making Change" usually refers to the problem of representing a given amount using the fewest coins or notes of specified denominations.


TASK

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)

Return: fewest number of coins needed to meet total

coins is a list of the values of the coins in your possession

The value of a coin will always be an integer greater than 0

You can assume you have an infinite number of each denomination of coin in the list

Your solution’s runtime will be evaluated in this task


Requirements

+ The file should start with #!/usr/bin/python3.

+ All files should end with a new line.

+ The code should adhere to PEP 8 style.

+ The function makeChange(coins, total) should determine the fewest number of coins needed to meet a given total.

+ If the total is 0 or less, return 0.

+ If total cannot be met by any number of coins you have, return -1.

+ The file containing the code must be an executable file.


Project Solution

The problem is about finding the minimum number of coins that you can use to make a certain total. If it's not possible to make that total with the coins you have, you should return -1.

To solve the problem, I used a dynamic programming approach. I built up an array dp of size total + 1 where dp[i] represents the minimum number of coins needed to get the total i.

For each total from 1 to the given total, I checked if I could reach that total by subtracting the value of each coin from the current total. I stored the minimum count of coins needed in the dp array.

Finally, I returned the value of dp[total]. If dp[total] is still infinity, that means it's impossible to reach the total with the given coins, so I returned -1.
