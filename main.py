#This is a python todo list app


tasks = []

def addTask():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def listTasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the task number to delete: "))
        if 0 <= taskToDelete < len(tasks):
            deleted_task = tasks.pop(taskToDelete)
            print(f"Task '{deleted_task}' has been deleted.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

if __name__ == "__main__":
    print("Welcome to the To-Do List App!")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            print("Goodbye 👋👋👋!")
            break
        else:
            print("Invalid choice. Please try again.")
