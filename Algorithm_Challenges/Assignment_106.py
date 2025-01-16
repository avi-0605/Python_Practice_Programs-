#106.Coin Change (DP) Solve the coin change problem using dynamic programming for an exact solutio
def coin_change(coins, target):
    # Initialize a list to store the minimum number of coins for each amount from 0 to target
    # Set a large number as the default (this represents "infinity", meaning the amount is not possible)
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # No coins needed to make 0 amount

    # Loop through each coin
    for coin in coins:
        # Update the dp list for amounts that can be made with the current coin
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the target amount can be made, return the number of coins; otherwise, return -1
    return dp[target] if dp[target] != float('inf') else -1

# List of available coin denominations
coins = [1, 5, 10, 25]
# The target amount to make
target = 63

# Output the result: minimum number of coins needed
print("Minimum coins needed:", coin_change(coins, target))
