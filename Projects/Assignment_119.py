#Dictionary App Use a dictionary file (or API) to create a simple command-line dictionary to look up words and their definitions.
# Simple Dictionary App

# Predefined dictionary with some words and their definitions
simple_dict = {
    "apple": "A fruit that grows on trees.",
    "banana": "A yellow fruit that's long and curved.",
    "cat": "A small domesticated carnivorous mammal.",
    "dog": "A domesticated carnivorous mammal with a bark.",
}

# Function to get the definition of a word
def get_definition(word):
    word = word.lower()
    if word in simple_dict:
        print(f"{word.capitalize()}: {simple_dict[word]}")
    else:
        print(f"Sorry, the word '{word}' is not in the dictionary.")

# Main program loop
def main():
    print("Welcome to the Simple Dictionary App!")
    while True:
        word = input("Enter a word to look up (or 'exit' to quit): ").lower()
        if word == "exit":
            print("Goodbye!")
            break
        get_definition(word)

if __name__ == "__main__":
    main()

