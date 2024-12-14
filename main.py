def Add():
    task = input("Add Tasks(will be in lower case)").lower()
    print(f"This is the task you entered: {task}")
    task_correct = input("Is this the task you entered? [y/n]").lower()

    if task_correct == "y":
        print("Adding task...")
        is_completed = "Not Completed"
        with open("list.txt", 'a') as f:
            f.write(task + "|" + is_completed + "\n")
    elif task_correct == "n":
        print("Asking again")
        Add()
    else:
        print("Invalid")
        Add()

def View():
    print("Here are the files (if nothing shows up means you have no saved to do lists)")

    for i in range(1,3):
        print()

    with open("list.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            print(data)


def Finish():
    task = input("Name of the task please").lower()

    print("Ok")
    
    with open("list.txt", 'r') as f:
        lines = f.readlines()
   
    with open("list.txt", 'w') as f:
        for line in lines:
            data = line.rstrip()  
            if data.startswith(task) and "Done" not in data:
                f.write(task + "|" + "Done" + "\n")
            else:
                f.write(line)
            



running = True

while running:
    print()
    print("**======To Do list=======**\n")
    print()
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Finish Task")
    print("4. Quit")

    try:
        mode = int(input("enter mode"))
    except:
        print("Enter a valid mode (enter number)")
        continue


    if mode == 1:
        Add()
    elif mode == 2:
        View()
    elif mode == 3:
        Finish()
    else:
        print("Ok Shutting down")
        running = False
        quit()
