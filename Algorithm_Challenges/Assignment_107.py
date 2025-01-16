#Knapsack Problem (0/1 DP) Implement the 0/1 Knapsack using dynamic programming.
def knapsack(values, weights, capacity):
    n = len(values)
    
    # DP table to store results of subproblems
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build the table in bottom-up manner
    for i in range(n + 1):
        for w in range(capacity + 1):
            # Base case: no items or zero capacity
            if i == 0 or w == 0:
                dp[i][w] = 0
            else:
                # If the current item's weight is less than or equal to the knapsack capacity
                if weights[i - 1] <= w:
                    # Max of including or excluding the item
                    dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
                else:
                    # If the current item can't be included
                    dp[i][w] = dp[i - 1][w]
    
    # The last cell contains the result
    return dp[n][capacity]


# Example usage
values = [60, 100, 120]  # Values of the items
weights = [10, 20, 30]  # Weights of the items
capacity = 50  # Capacity of the knapsack

print("Maximum value in Knapsack =", knapsack(values, weights, capacity))
