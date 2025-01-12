# Element-wise Sum of Two List Given two lists of equal length, create a third list that stores the element-wise sum.

def element_wise_sum(list1, list2):
    if len(list1)!=len(list2):
        return "The lists must be of equal length."
    sum_list = [list1[i]+list2[i] for i in range(len(list1))]
    return sum_list
list1 = input("Enter the first list (e.g., [1, 2, 3]): ")
list2 = input("Enter the second list (e.g., [4, 5, 6]): ")
list1 = eval(list1)
list2 = eval(list2)
result = element_wise_sum(list1,list2)
print("Element-wise Sum:", result)

