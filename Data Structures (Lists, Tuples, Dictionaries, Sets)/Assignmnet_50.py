# Set Membership Testing Given a set of names, prompt the user for a name. Check if it is in the set or not.
def check_name_in_set():

    names_set = {'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack'}
    
    print("Available names:", sorted(names_set))
    
    name = input("\nEnter a name to check (or press Enter to exit): ").strip().capitalize()
    if not name:
        print("Goodbye!")
        return
    
    if name in names_set:
        print(f"Yes, '{name}' is in the set!")
    else:
        print(f"No, '{name}' is not in the set.")
        check_name_in_set() 
check_name_in_set()

