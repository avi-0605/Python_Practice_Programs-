# #Search for a Word in a File Prompt the user for a word and search for it in a file. Return the line number(s) where it appears.
def search_word_in_file(word):
    try:
        with open('output.txt', 'r') as file:
            lines = file.readlines()

        word = word.lower()  # Make the search case-insensitive
        found = False
        line_num = 1  # Manually track the line number

        for line in lines:
            if word in line.lower():
                print(f"Line {line_num}: {line.strip()}")
                found = True
            line_num += 1  # Increment line number manually

        if not found:
            print(f"'{word}' not found in the file.")

    except FileNotFoundError:
        print("Error: The file 'output.txt' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
word = input("Enter the word to search: ")
search_word_in_file(word)