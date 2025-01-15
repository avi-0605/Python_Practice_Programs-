#Read from File Read the content of "output.txt" (from the above problem) and print it to the con
with open("output.txt", "r") as file:
    content=file.read()
    print("Content of output.txt:",content)
