# Tuple to List Convert a user-defined tuple to a list, modify it, and convert it back to a tuple.
# Convert a tuple to a list, modify it, and convert it back to a tuple

def modify_tuple(tup):
    list_version=list(tup)
    index=int(input("Enter the index of the element to modify: "))
    new_value = input("Enter the new value: ")
    if 0 <= index < len(list_version):
        list_version[index]=new_value
    else:
        return "Invalid index"
    modified_tuple=tuple(list_version)
    return modified_tuple
user_tuple=("apple", "banana", "cherry", "date")
modified_tuple=modify_tuple(user_tuple)
print("Modified Tuple:", modified_tuple)
