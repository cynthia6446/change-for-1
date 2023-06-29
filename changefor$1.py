# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:48:24 2023

@author: be
"""
def count_ways(coins, n, amount):
    
    # Create a table to store the results
    
    table = [[0] * (amount + 1) for _ in range(n + 1)]
    
    # If the amount is 0, there is one way to make the change (using no coins)
    for i in range(n + 1):
        table[i][0] = 1
        
    # Calculate the number of ways for each coin denomination
    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if coins[i - 1] <= j:
                table[i][j] = table[i - 1][j] + table[i][j - coins[i - 1]]
            else:
                    table[i][j] = table[i - 1][j]
            
    return table[n][amount]



coins = [1, 5, 10, 25, 50] # Denominations of coins available
n = len(coins) # Number of coin denominations
amount = 100 # Total amount in cents (e.g., $1 = 100 cents)

# Calculate the number of different ways to make the change
num_ways = count_ways(coins, n, amount)

print(f"The number of different ways to make a dollar is: {num_ways}")
