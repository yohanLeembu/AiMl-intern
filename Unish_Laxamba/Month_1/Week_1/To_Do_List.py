# Main source of storage
to_do_list = []

# Function to add the tasks in the list
def add_items():
    task = input('Enter the task: ')
    print(' ')
    to_do_list.append(task)
    print('Successfully added the task.\n')

# Function to view the available tasks stored in the list.
def view_tasks():

    # Using the if else statement to view the available tasks.
    if len(to_do_list) == 0:
        return 'The whole list is empty. Please add the tasks.'
    else:
        print('----Tasks----')
        for key, task in enumerate(to_do_list):
            print(f'{key}. {task}')
        print(' ')

# Function to delete the tasks from the list.
def delete_tasks():
    if len(to_do_list) == 0:
        return 'The whole list is empty. Please add the tasks.'
    else:
        print('----Tasks----')
        for key, task in enumerate(to_do_list):
            print(f'{key}. {task}')
        print(' ')
        index = int(input('Enter the index of the tasks you want to delete: '))
        del to_do_list[index]
        print('Successfully deleted the task.\n')


# Main function to interact with the users    
def choices():
    while True:
        print('Enter 1 for adding the task.')
        print('Enter 2 for viewing the task.')
        print('Enter 3 for deleting the task.')
        print('Enter 4 to exit. ')
        print(' ')

        choice = input('Enter your choice: ')
        print(' ')

        if choice in ['4']:
            break
        if choice in ['1', '2', '3']:

            if choice == '1':
                add_items()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                delete_tasks()
        else:
            print('Enter the right choice.')

# Running the main function
choices()