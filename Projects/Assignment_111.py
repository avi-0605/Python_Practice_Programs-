#Simple Password Generator Generate a random password of a specified length with letters, digits, and special characters.
import random
import string

def generate_password(length):
    # Define characters (letters, digits, special characters)
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Combine all characters
    all_characters = letters + digits + special_characters
    
    # Generate password by randomly selecting characters
    password = ''
    for _ in range(length):
        password += random.choice(all_characters)
    
    return password

# Example usage
length = 12
password = generate_password(length)
print("Generated Password:", password)
