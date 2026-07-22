def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


def add_task(tasks):
    task = input("Enter a new task: ")

    if task.strip() == "":
        print("Task cannot be empty!")
    else:
        tasks.append(task)
        print("Task added successfully.")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed = tasks.pop(task_number - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = []

    while True:
        show_menu()

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            remove_task(tasks)

        elif choice == "4":
            print("Thank you for using the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()