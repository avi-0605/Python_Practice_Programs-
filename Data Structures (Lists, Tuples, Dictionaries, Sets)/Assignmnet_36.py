# Remove Duplicates from a List Prompt for a list of integers (possibly with duplicates). Create a new list with duplicates removed.

numbers=input("Enter numbers: ").split()
number=[int(n) for n in numbers]
unique_numbers=list(set(number))
print("Unique numbers:", unique_numbers)
