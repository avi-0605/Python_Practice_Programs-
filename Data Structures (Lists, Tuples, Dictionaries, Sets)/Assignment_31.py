#List Operation Create a list of integers. Perform append, insert, remove, pop, and display the list at each stage.\
numbers = [1, 2, 3, 4, 5]
print("Initial list:", numbers)

numbers.append(6)
print("After append:", numbers)

numbers.insert(2, 10)
print("After insert at index 2:", numbers)

numbers.remove(3)
print("After removing 3:", numbers)

popped_element=numbers.pop()
print("After pop:", numbers)
print("Popped element:", popped_element)
