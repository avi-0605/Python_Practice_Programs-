# Set Operations Prompt the user for two lists, convert them to sets, and then display the union, intersection, and difference of these sets.
def set_operations():
        list1 = input("Enter first list elements separated by spaces: ").split()
        list2 = input("Enter second list elements separated by spaces: ").split()
        set1 = set(list1)
        set2 = set(list2)
        print("Set 1:", set1)
        print("Set 2:", set2)
        print("Set Operations:")
        print("Union:", set1.union(set2))
        print("Intersection:", set1.intersection(set2))
        print("Difference (Set1 - Set2):", set1.difference(set2))
        print("Difference (Set2 - Set1):", set2.difference(set1))
        print("Symmetric Difference:", set1.symmetric_difference(set2))

set_operations()