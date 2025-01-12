# Find Common Elements of Two Lists Given two lists, find the common elements and store them in a new list.

def find_common_elements(list1, list2):
    common=list(set(list1) & set(list2))
    return common
list1=input("Enter the first list : ")
list2=input("Enter the second list : ")
common_elements =find_common_elements(list1,list2)
print("Common Elements:",common_elements)
