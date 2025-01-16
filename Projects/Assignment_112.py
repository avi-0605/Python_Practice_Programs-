#Contact Book Write a program to store contact details (name, number, email) in a file and allow adding/searching.
def add_contact():
    with open("contacts.txt", "a") as file:
        name = input("Enter name: ")
        number = input("Enter phone number: ")
        email = input("Enter email: ")
        file.write(f"{name},{number},{email}\n")
        print("Contact added successfully!")

def search_contact():
    name_to_search = input("Enter the name to search: ")
    with open("contacts.txt", "r") as file:
        found = False
        for line in file:
            name, number, email = line.strip().split(',')
            if name.lower() == name_to_search.lower():
                print(f"Found: {name}, {number}, {email}")
                found = True
                break
        if not found:
            print("Contact not found.")

def main():
    while True:
        print("\n1. Add Contact\n2. Search Contact\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

main()  # Directly call the main function
