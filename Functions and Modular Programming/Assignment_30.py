#Write a function count_occurrences(lst, x) that returns how many times x appears in the list lst.
def count_occurrences(lst, x):
    return lst.count(x)
input_list=input("Enter a list of numbers (separated by spaces): ").split()
input_list= [int(i) for i in input_list]  
x = int(input("Enter the number to count occurrences of: "))
result = count_occurrences(input_list, x)
print(f"The number",x," appears",result,"times in the list.")
