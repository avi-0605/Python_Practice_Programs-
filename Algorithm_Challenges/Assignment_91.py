# Bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, no need to check them again
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:  # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
print(numbers)
bubble_sort(numbers)
print("Sorted List:", numbers)
