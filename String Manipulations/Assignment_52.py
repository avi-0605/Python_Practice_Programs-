# Palindrome String Checker Check if a given string is a palindrome (case-sensitive or case-insensitive based on your choice).

def is_palindrome(string):
    string=string.lower()
    return string==string[::-1]

user_input=input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(user_input," is a palindrome.")
else:
    print(user_input,"is not a palindrome.")
