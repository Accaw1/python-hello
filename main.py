"""Command-line todo list manager for operations coordinators.

Run with:  python main.py
Uses only the Python standard library.
"""

import csv
import os

TODOS_FILE = "todos.csv"

todos = []


def add_one_task(title):
    """Append a new task to the in-memory list. Returns True if added."""
    title = title.strip()
    if not title:
        print("Task title cannot be empty.")
        return False
    todos.append(title)
    print(f"Added: {title}")
    return True


def print_list():
    """Print every task with a 1-based position users can reference."""
    if not todos:
        print("There are no pending tasks.")
        return
    print("Pending tasks:")
    for position, task in enumerate(todos, start=1):
        print(f"  {position}. {task}")


def delete_task(number_to_delete):
    """Remove the task at the given 1-based position. Returns True if deleted."""
    try:
        position = int(number_to_delete)
    except (TypeError, ValueError):
        print("Please enter a valid task number.")
        return False
    if position < 1 or position > len(todos):
        print(f"No task at position {position}.")
        return False
    removed = todos.pop(position - 1)
    print(f"Deleted: {removed}")
    return True


def save_todos():
    """Write the current tasks to todos.csv, one task per row."""
    with open(TODOS_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for task in todos:
            writer.writerow([task])
    print(f"Saved {len(todos)} task(s) to {TODOS_FILE}.")


def load_todos():
    """Replace the in-memory tasks with those stored in todos.csv."""
    if not os.path.exists(TODOS_FILE):
        print(f"{TODOS_FILE} not found. Nothing to load.")
        return False
    loaded = []
    with open(TODOS_FILE, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if row and row[0].strip():
                loaded.append(row[0])
    todos[:] = loaded
    print(f"Loaded {len(todos)} task(s) from {TODOS_FILE}.")
    return True


MENU = """
Choose an option:
    1. Add one task
    2. Delete a task
    3. Print the current list of tasks
    4. Save the todos to todos.csv
    5. Load todos from todos.csv
    6. Exit
"""


def main():
    print("Welcome to the Todo List CLI!")
    while True:
        print(MENU)
        try:
            option = input("Option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break

        if option == "1":
            add_one_task(input("What is your task? "))
        elif option == "2":
            print_list()
            if todos:
                delete_task(input("Which task number do you want to delete? "))
        elif option == "3":
            print_list()
        elif option == "4":
            save_todos()
        elif option == "5":
            load_todos()
        elif option == "6":
            print("Bye!")
            break
        else:
            print("Invalid option, please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
