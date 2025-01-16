#Hangman Game Implement the “Hangman” word-guessing game using loops and conditionals.
import random

def hangman():
    # List of simple words
    words = ["apple", "banana", "grape", "orange", "kiwi"]
    
    # Choose a random word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # Create a list to store guessed letters
    attempts = 6  # Number of attempts
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("Word:", " ".join(guessed_word))
        guess = input("Guess a letter: ").lower()
        
        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct!")
            # Update the guessed_word list
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")
        
        # Check if the word is completely guessed
        if "_" not in guessed_word:
            print("Congratulations! You guessed the word:", word)
            break
    
    if attempts == 0:
        print("Game over! The word was:", word)

# Start the game
hangman()
