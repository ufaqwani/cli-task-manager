tasks = ["code", "build project", "apply to roles", "check mails"]
tries = 0

for index, task in enumerate(tasks, 1):
    print(f"{index}. {task}")
print(f"You have {len(tasks)} total tasks")
user_selection = input("Do you want to add a task? Press Y for yes and N for no: ")
if user_selection == "Y".lower():
    new_task = input("Enter the task: ")
    tasks.append(new_task)
    print("Task Added")
elif user_selection == "N".lower():

    delete_task = input("Do you want to mark your tasks as done? Press Y for yes and N for no: ")
    if delete_task == "Y".lower():
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
        while tries < 3:    
            pop_selection = input("Select the task number to mark it off: ")
            task_index = int(pop_selection) - 1
            if 0 <= task_index < len(tasks):
                tasks.pop(task_index)
                print("Task removed")
                break
            else:
                tries += 1
                print("Invalid task number. Try again")
                if tries == 3:
                    print("You have exhasuted the number of tries allowed")