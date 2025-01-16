#Permutations of a List Generate all permutations of a given list of distinct elements.
import itertools  # Importing the itertools module, which provides a permutations function

def generate_permutations(lst):
    # itertools.permutations generates all possible permutations of the list
    # It returns an iterator, so we convert it to a list before returning
    return list(itertools.permutations(lst))

# Example usage
lst = [1, 2, 3]  # Define a list of distinct elements
permutations = generate_permutations(lst)  # Call the function to generate permutations
print(permutations)  # Print the list of permutations
