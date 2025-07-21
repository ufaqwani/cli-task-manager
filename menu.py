#store the number of tasks
tasks = []

#lists the menu options

full_menu = ["View Tasks", "Add Task", "Remove Tasks", "Exit"]

#iterates the lists and starts the while loop
while True:
    for index, menu in enumerate(full_menu, 1):
        print(f"{index}.{menu}")
    #Asks the user for option selection
    try:
        selection = int(input("Please select a relevant option from 1 to 4: "))
    except ValueError:
        print("Invalid Option, Please Enter Relevant Number.\n")
        continue
    if selection == 1:
        if not tasks:
                print("No tasks. Please add some tasks\n")
        else:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}\n")
    elif selection == 2:
        new_task = input("Please Enter the Task Name: ").lower().strip()
        tasks.append(new_task)
        print("Task added Successfully\n")
    
    elif selection == 3:
        while True:
            if not tasks:
                print("No tasks. Please add some tasks first\n")
                break
            else:
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    print("Enter the task number to remove it.")
                    print("Enter 0 to return to the main menu.\n") 
                try:
                    pop_task = int(input("Please type the task number to be removed from the list or press 0 to go back to the main menu: "))
                    if pop_task == 0:
                        print("Returning to main menu...\n")
                        break  # Break removal loop and go to main menu
                    task_index = int(pop_task) - 1
                    if 0 <= task_index < len(tasks):
                        removed_task = tasks.pop(task_index)
                        print(f"Task {removed_task} was removed successfuly\n")
                    else:
                        print("Invalid task number\n")
                except ValueError:
                    print("Invalid Option, Please Enter Relevant Number\n")
                
    elif selection == 4:
        print("Goodbye")
        break
    else:
        print("Invalid Input, Please Try Again\n")