#Copy File Copy the contents of one text file to another. Handle exceptions if the source file does not exis"The source file does not exist.")
try:
    with open("output.txt", "r") as source:
        content = source.read()
    with open("copy.txt", "w") as target:
        target.write(content)
    print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
print(content)