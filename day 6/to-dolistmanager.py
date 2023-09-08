
task_file = "tasks.txt"

def add_task(task):
    with open(task_file, "a") as file:
        file.write(task + "\n")


def view_tasks():
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
        if tasks:
            print("To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("Your to-do list is empty.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


def mark_task_completed(task_number):
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1] = tasks[task_number - 1].replace("[ ]", "[x]")
            with open(task_file, "w") as file:
                file.writelines(tasks)
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


def remove_completed_tasks():
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
        tasks = [task for task in tasks if "[ ]" in task]
        with open(task_file, "w") as file:
            file.writelines(tasks)
        print("Completed tasks removed.")
    except FileNotFoundError:
        print("Your to-do list is empty.")


while True:
    print("Choose an action:")
    print("1 - Add task")
    print("2 - View tasks")
    print("3 - Mark task as completed")
    print("4 - Remove completed tasks")
    print("5 - Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        task = input("Enter the task: ")
        add_task(f"[ ] {task}")
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_number = int(input("Enter the task number to mark as completed: "))
        mark_task_completed(task_number)
    elif choice == "4":
        remove_completed_tasks()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
