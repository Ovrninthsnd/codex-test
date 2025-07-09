todo_list = []


def show_menu():
    print("\nTo-Do List")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")


def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added.")


def remove_task():
    view_tasks()
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        removed = todo_list.pop(index)
        print(f"Removed: {removed}")
    except (IndexError, ValueError):
        print("Invalid task number.")


# Main loop
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
