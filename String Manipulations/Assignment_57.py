# String Case Conversion Convert a given string to upper case, lower case, and title case. Print all three versions.
def string_case_conversion(string):
    upper_case = string.upper()
    lower_case = string.lower()
    title_case = string.title()
    return upper_case, lower_case, title_case

user_input = input("Enter a string: ")

upper, lower, title = string_case_conversion(user_input)
print("Upper case:", upper)
print("Lower case:", lower)
print("Title case:", title)
