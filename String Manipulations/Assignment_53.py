#Count Vowels in a String Count how many vowels (a, e, i, o, u) appear in a string.

def count_vowels(string):
    count = 0
    for char in string:
        if char in 'aeiouAEIOU':
            count += 1
    return count

user_input = input("Enter a string: ")

print("Number of vowels:", count_vowels(user_input))

