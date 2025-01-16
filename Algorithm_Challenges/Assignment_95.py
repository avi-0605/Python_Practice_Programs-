#Quick Sort Implement quick sort to sort a list of integers.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: if the list is empty or has one element, it's already sorted

    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    left = [x for x in arr if x < pivot]  # Elements less than pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to pivot
    right = [x for x in arr if x > pivot]  # Elements greater than pivot

    # Recursively apply quick_sort to the left and right parts
    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = quick_sort(numbers)
print("Sorted List:", sorted_numbers)
