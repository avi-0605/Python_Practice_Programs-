# Dictionary: Student Grades Create a dictionary with student names as keys and their grades as values. Prompt the user for a name and display the grade.
def manage_grades():
    grades1 = {}
    
    while True:
        print("\n1. Add grade")
        print("2. Show grade")
        print("3. Display all grades")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            grade = float(input("Enter grade: "))
            grades1[name] = grade
            print("Grade added for", name)
                
        elif choice == '2':
            name = input("Enter student name: ")
            print(name + "'s grade:", grades1.get(name, 'Not found'))
                
        elif choice == '3':
            if grades1:
                for name, grade in sorted(grades1.items()):
                    print(name + ":", grade)
            else:
                print("No grades recorded.")
                
        elif choice == '4':
            print("Exiting...")
            break
            
        else:
            print("Invalid choice! Enter 1-4.")
manage_grades()
