def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the index of the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
selection_sort(numbers)
print("Sorted List:", numbers)
