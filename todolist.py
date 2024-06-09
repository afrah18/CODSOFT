import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found!")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['description']} - {'Done' if task['done'] else 'Not done'}")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "done": False})
    print("Task added successfully!")

def update_task(tasks):
    show_tasks(tasks)
    try:        
        idx = int(input("Enter task number to update: ")) - 1
        task = tasks[idx]
        task["done"] = not task["done"]
        print("Task updated successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        del tasks[idx]
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid task number!")


tasks = load_tasks()

while True:
    print("\nTo-Do List:")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        show_tasks(tasks)   # calling the show task method
    elif choice == "2":
        add_task(tasks)     # calling the add task method
    elif choice == "3":
        update_task(tasks)  # calling the update task method
    elif choice == "4":
        delete_task(tasks)  # calling the delete task method
    elif choice == "5":
        save_tasks(tasks)   # calling the save task method
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")

# OUTPUT:-

# To-Do List:
# 1. Show Tasks
# 2. Add Task
# 3. Update Task
# 4. Delete Task
# 5. Exit
# Enter your choice: 2
# Enter task description: Codesot taks
# Task added successfully!

# To-Do List:
# 1. Show Tasks
# 2. Add Task
# 3. Update Task
# 4. Delete Task
# 5. Exit
# Enter your choice: 3
# Tasks:
# 1. Codesot taks - Not done
# Enter task number to update: 1
# Task updated successfully!

# To-Do List:
# 1. Show Tasks
# 2. Add Task
# 3. Update Task
# 4. Delete Task
# 5. Exit
# Enter your choice: 1
# Tasks:
# 1. Codesot taks - Done

# To-Do List:
# 1. Show Tasks
# 2. Add Task
# 3. Update Task
# 4. Delete Task
# 5. Exit
# Enter your choice: 4
# Tasks:
# 1. Codesot taks - Done
# Enter task number to delete: 1
# Task deleted successfully!

# To-Do List:
# 1. Show Tasks
# 2. Add Task
# 3. Update Task
# 4. Delete Task
# 5. Exit
# Enter your choice: 5
# Exiting...
