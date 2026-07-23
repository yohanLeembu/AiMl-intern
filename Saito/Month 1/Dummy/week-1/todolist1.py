def show_menu():
    print("\nTO -DO list")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")

    if task.strip() == "":
        print("task cant be empty!")
    else:
        tasks.append(task)
        print("task addded successfully:")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
    else:
        print("\nYou Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to be removed: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task removed: {removed}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")

def main():
    task =[]

    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")
        if choice == "1":
            add_task(task)

        elif choice == "2":
            view_tasks(task)

        elif choice == "3":
            remove_task(task)

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
