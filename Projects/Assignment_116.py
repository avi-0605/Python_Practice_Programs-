# Text-based Adventure Create a small text-based adventure game with multiple rooms and user choices.
def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a small room with two doors.")
    
    # Start in the first room
    room1()

def room1():
    print("\nYou are in Room 1. There are two doors: one to the left and one to the right.")
    print("1. Go through the left door.")
    print("2. Go through the right door.")
    
    choice = input("What do you want to do? (1/2): ")
    
    if choice == "1":
        room2()
    elif choice == "2":
        room3()
    else:
        print("Invalid choice. Try again.")
        room1()

def room2():
    print("\nYou enter Room 2. It's dark and you hear a strange noise.")
    print("1. Turn on the light.")
    print("2. Leave the room and go back to Room 1.")
    
    choice = input("What do you want to do? (1/2): ")
    
    if choice == "1":
        print("You turn on the light and find a treasure chest! You win!")
    elif choice == "2":
        room1()
    else:
        print("Invalid choice. Try again.")
        room2()

def room3():
    print("\nYou enter Room 3. It looks like a dead end.")
    print("1. Try to open the door on the other side of the room.")
    print("2. Go back to Room 1.")
    
    choice = input("What do you want to do? (1/2): ")
    
    if choice == "1":
        print("The door opens, and you escape the room. You win!")
    elif choice == "2":
        room1()
    else:
        print("Invalid choice. Try again.")
        room3()

# Start the game
start_game()
