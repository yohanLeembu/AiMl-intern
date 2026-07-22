tasks = []
while True:
    print("<<<<TO-DO List>>>>")
    print('1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit')
    choice = int(input('Enter your choice: '))
    
    
    if choice == 1:
        task = input('Enter the task: ')
        tasks.append(task)
        
    elif choice == 2:
        if not tasks:
            print('nothing')
        else:
            for i,task in enumerate(tasks,1):
                print(i,'. ',task)

    elif choice == 3:
        if not tasks:
            print('nothing')
            continue
        else:
            for i,task in enumerate(tasks,1):
                print(i,'. ',task)
        remove = int(input('no. of the task you want to remove: '))
        if len(tasks) >= remove:
            tasks.pop(remove-1)
        else: 
            print('invalid input')

    elif choice == 4:
        break


    