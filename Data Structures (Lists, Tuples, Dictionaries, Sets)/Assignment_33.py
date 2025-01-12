# Second Largest Element In a list of unique integers, find the second largest element.
def second_largest(lst):
    if len(lst) < 2:
        return None  
    lst.sort()  
    return lst[-2]  
lst = []
lst1 = input("Enter a list of numbers: ").split()
for i in lst1:
    lst.append(int(i))
print("Second largest:", second_largest(lst1))