#Prompt the user for some text and append it to "output.txt" without overwriting existing content.
try:
    append_text = input("Enter text to append: ")
    with open("output.txt", "a") as file:
        file.write(append_text + "\n")
    print("Text appended successfully.")
except FileNotFoundError:
    print("Source file not found.")
