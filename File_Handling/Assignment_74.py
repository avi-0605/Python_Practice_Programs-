#Count Lines in a File Read a text file and count how many lines it contains.
try:
    with open("output.txt", "r") as source:
        lines = source.readlines()
        line_count = len(lines)
    print(f"The file contains {line_count} lines.")
except FileNotFoundError:
    print("Source file not found.")
