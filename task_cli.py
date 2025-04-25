import json
import os
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"


def now():
    return datetime.now().isoformat()


def load_tasks_from_file():
    if not os.path.exists(TASKS_FILE):
        return {"tasks": []}
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks_to_file(tasks_data):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks_data, file, indent=4)


def list_tasks(filter_status=None):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] [{task['status']}] [{task['description']}]")


def add_task(description):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    new_task = {
        "id": len(tasks_data["tasks"]) + 1,
        "description": description,
        "status": "todo",
        "createdAt": now(),
        "updatedAt": now(),
    }
    tasks.append(new_task)
    save_tasks_to_file({"tasks": tasks})
    print(f"Task added successfully (ID: {new_task['id']})")


def update_task(task_id, description):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updatedAt"] = now()
            save_tasks_to_file({"tasks": tasks})
            print(f"Task {task_id} updated.")
            return
    print(f"No task with ID {task_id} found.")


def delete_task(task_id):
    try:
        task_id = int(task_id)
    except ValueError:
        print("Error: El ID debe ser un número válido.")
        return
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print(f"No task with ID {task_id} found.")
    else:
        save_tasks_to_file({"tasks": new_tasks})
        print(f"Task {task_id} deleted.")


def mark_status(task_id, status):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = now()
            save_tasks_to_file({"tasks": tasks})
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"No task with ID {task_id} found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [options]")
        return
    command = sys.argv[1]
    try:
        if command == "add":
            if len(sys.argv) > 2:
                add_task(" ".join(sys.argv[2:]))
            else:
                print("You must provide a description for the task.")
        elif command == "update":
            update_task(int(sys.argv[2]), sys.argv[3])
        elif command == "delete":
            delete_task(int(sys.argv[2]))
        elif command == "mark-in-progress":
            mark_status(int(sys.argv[2]), "in-progress")
        elif command == "mark-done":
            mark_status(int(sys.argv[2]), "done")
        elif command == "list":
            if len(sys.argv) > 2:
                list_tasks(sys.argv[2])
            else:
                list_tasks()
        else:
            print("Unknown command or missing arguments.")
    except ValueError:
        print("Invalid ID. It should be a number.")


if __name__ == "__main__":
    main()
