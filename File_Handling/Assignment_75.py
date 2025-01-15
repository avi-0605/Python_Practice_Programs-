# Count Words in a File Read a text file and count how many words it contain]
try:
    with open("output.txt", "r") as source:
        content = source.read()
        word_count = len(content.split())
    print("The file contains",word_count,"words.")
except FileNotFoundError:
    print("Source file not found.")
