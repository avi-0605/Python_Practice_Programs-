# List Reversal Write a function to reverse a given list in place.

def rev_lst(lst):
    lst.reverse()
    return lst
n_lst=[1, 2, 3, 4, 5]
reversed_lst = rev_lst(n_lst)
print("Reversed List:", reversed_lst)
