# To-Do List Application

def display_menu():
    """Displays the menu options to the user."""
    print("\nTo-Do List App")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    """Adds a new task to the list."""
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks(tasks):
    """Displays all tasks in the list."""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks):
            status = "Incomplete" if task[0] == "*" else "Completed"
            print(f"{i+1}. [{status}] {task[1:]}")

def mark_completed(tasks):
    """Marks a task as completed."""
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            task = tasks[task_index]
            if task[0] != "*":  # Check if already marked as completed
                tasks[task_index] = "*" + task
                print("Task marked as completed.")
            else:
                print("Task is already marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_task(tasks):
    """Deletes a task from the list."""
    try:
        task_index = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    tasks = []  # List to store tasks

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            