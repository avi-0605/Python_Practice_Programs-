def linear_search(arr, target):
    for i in (len(arr))
    element=arr[i]
        if element == target:
            return index  # Return the index if element is found
    return -1  # Return -1 if the target is not found

# Example usage:
numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22
index = linear_search(numbers, target)

if index != -1:
    print(f"Element {target} found at index {index}.")
else:
    print(f"Element {target} not found.")
