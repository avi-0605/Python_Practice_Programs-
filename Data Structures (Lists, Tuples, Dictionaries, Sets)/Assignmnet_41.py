#Tuple Creation and Access Create a tuple of strings. Prompt the user for an index and print the element at that index.

def access_element(tup, index):
    if index < 0 or index >= len(tup):
        return "Invalid index. Please provide a valid index."
    return tup[index]

tuple_s=("apple", "banana", "cherry", "date", "strawberry")
index=int(input("Enter an index to access an element from the tuple (0-4): "))

# Get the element at the provided index
result = access_element(tuple_s, index)
print("Element at index", index, ":", result)
