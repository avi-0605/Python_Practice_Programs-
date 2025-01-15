# 71.Write to File Prompt the user for a string and write it to a text file named "output.txt".
a=input("Enter a string: ")
with open("input.txt", "w") as file:
    file.write(a)
print("The input has been saved to output.txt")


