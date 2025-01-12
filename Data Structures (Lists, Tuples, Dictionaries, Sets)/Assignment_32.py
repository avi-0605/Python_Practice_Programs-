#Maximum and Minimum in a List Take a list of numbers from the user and find the maximum and minimum values.
lst = []
lst1 = input("Enter a list of numbers: ").split()
for i in lst1:
    lst.append(int(i))
print("Maximum:", max(lst))
print("Minimum:", min(lst))
