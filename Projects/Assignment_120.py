#Basic To-Do List Manager Allow users to add tasks, mark them as done, and view tasks. Store tasks in a file or in memory.
# Basic To-Do List Manager

# List to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append({"task": task, "done": False})
    print(f"Task '{task}' added.")

# Function to mark a task as done
def mark_done(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print(f"Task '{tasks[task_index]['task']}' marked as done.")
    else:
        print("Invalid task index.")

# Function to view all tasks
def view_tasks():
    if not tasks:
        print("No tasks added yet.")
        return
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

# Main program
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Mark Task as Done")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        view_tasks()
        try:
            task_index = int(input("Enter the task number to mark as done: "))
            mark_done(task_index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the To-Do List Manager.")
        break
    else:
        print("Invalid choice. Please try again.")
