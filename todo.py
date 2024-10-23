import json
import os

TODO_FILE = "todo_list.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f)


def add_tasks(tasks):
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks)
    print(f"Task '{description}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nTo-do List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{i}. {task['description']} - {status}")
    print()


def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num]["completed"] = True
            save_tasks(tasks)
            print(f"Task '{tasks[task_num]['description']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            save_tasks(tasks)
            print(f"Task '{deleted_task['description']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please eneter a valid number.")


def todo_manager():
    tasks = load_tasks()
    while True:
        print("\nTodo List Manager:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    todo_manager()
