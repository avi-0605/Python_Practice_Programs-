#Binary Search Implement binary search on a sorted list to find a given element.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        
        if arr[mid] == target:  # If the target is found, return the index
            return mid
        elif arr[mid] < target:  # If target is larger, search in the right half
            low = mid + 1
        else:  # If target is smaller, search in the left half
            high = mid - 1

    return -1  # Return -1 if the target is not found

# Example usage:
sorted_list = [11, 12, 22, 25, 34, 64, 90]
target = 22
index = binary_search(sorted_list, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")
