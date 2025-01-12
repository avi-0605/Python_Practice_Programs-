# Remove Spaces Remove all spaces from a given string ("Hello World" -> "HelloWorld").

def remove_spaces(string):
    return string.replace(" ", "")

user_input = input("Enter a string: ")

print("String without spaces:", remove_spaces(user_input))
