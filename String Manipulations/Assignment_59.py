#Count Special Characters Prompt the user for a string and count the number of punctuation/special characters (like !, @, #, etc.).
import string

def count_special_characters(input_str):
    count = 0
    for char in input_str:
        if char in '!@#,.':
            count += 1
    return count

# Example usage:
input_string = input("Enter a string: ")
special_char_count = count_special_characters(input_string)
print(f"Number of special characters: {special_char_count}")
