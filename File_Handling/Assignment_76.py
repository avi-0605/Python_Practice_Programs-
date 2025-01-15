# Find Longest Line in a File Find and print the longest line in a given text file.
try:
    with open("output.txt", "r") as source:
        lines = source.readlines()
        longest_line = max(lines, key=len).strip()
    print(f"The longest line is: {longest_line}")
except FileNotFoundError:
    print("Source file not found.")
