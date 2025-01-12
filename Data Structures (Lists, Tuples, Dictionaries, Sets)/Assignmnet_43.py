# Check if Element Exists in Tuple Prompt the user for an element and check if it exists in the tuple.

user_tuple = ("apple", "banana", "cherry", "date")
element = input("Enter an element to check if it exists in the tuple: ")
if element in user_tuple:
    print(f"The element ",element,"exists in the tuple.")
else:
    print(f"The element ",element,"does not exist in the tuple.")

