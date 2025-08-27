# Task 3
# Develop a small CLI to-do list app that: Adds,removes,
# and displays tasks Saves all tasks in atasks.json file Loads tasks
# from file on startup
# 🛠 Concepts: json, lists, file handling, functions
# 🎯 Goal: Work with structured data and persistentstorage in JSON.

import json


def load_tasks():
    """Loads tasks from the tasks.json file."""
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        # Return an empty list if the file doesn't exist or is empty/corrupt
        return []


def save_tasks(tasks):
    """Saves the current list of tasks to the tasks.json file."""
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully!")


def display_tasks(tasks):
    """Displays the current list of tasks."""
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- Your To-Do List ---")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print("-----------------------\n")


def add_task(tasks):
    """user to add a new task."""
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added.")


def remove_task(tasks):
    """user to remove a task by its number."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the number of the task to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"'{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def Todo():
    """Main function for the CLI To-Do app."""
    tasks = load_tasks()

    while True:
        print("--- Menu ---")
        print("1. Add a new task")
        print("2. Display all tasks")
        print("3. Remove a task")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    Todo()
