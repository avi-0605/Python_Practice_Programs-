# Merge Two Dictionaries Given two dictionaries, merge them into a new dictionary.

def merge_dictionaries():
    dict1 = {}
    print("Enter key-value pairs for first dictionary:")
    while True:
        key = input("Enter key: ")
        if not key:
            break
        value = input("Enter value: ")
        dict1[key] = value


    dict2 = {}
    print("Enter key-value pairs for second dictionary :")
    while True:
        key = input("Enter key: ")
        if not key:
            break
        value = input("Enter value: ")
        dict2[key] = value
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Merged dictionary:", merged_dict)
merge_dictionaries()
