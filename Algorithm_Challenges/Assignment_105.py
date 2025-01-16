#Coin Change (Greedy)Given a list of coin denominations and a target amount, find the minimum number of coins needed using a greedy approach.
def coin_change_greedy(coins, target):
    # Sort coins in descending order to try larger denominations first
    coins.sort(reverse=True)
    count = 0
    
    # Iterate through each coin denomination
    for coin in coins:
        # Use as many of the current coin as possible
        count += target // coin
        # Reduce the target by the value taken
        target %= coin
    
    # If target is 0, return the number of coins used, else return -1 for failure
    return count if target == 0 else -1

# List of coin denominations and the target amount
coins = [1, 5, 10, 25]
target = 63
# Print the minimum number of coins needed
print("Minimum coins needed:", coin_change_greedy(coins, target))
