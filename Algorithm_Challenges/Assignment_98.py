import random

def knuth_shuffle(arr):
    for i in range(len(arr) - 1, 0, -1):
        # Select a random index from 0 to i
        j = random.randint(0, i)
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
knuth_shuffle(numbers)
print("Shuffled List:", numbers)
