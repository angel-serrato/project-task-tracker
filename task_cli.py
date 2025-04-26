import json
import os
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"


def main():
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [options]")
        return
    command = sys.argv[1]
    try:
        if command == "add":
            if len(sys.argv) < 3:
                raise ValueError("Usage: add [description]")
            add_task(" ".join(sys.argv[2:]))
        elif command == "update":
            if len(sys.argv) < 4:
                raise ValueError("Usage: update <id> [description]")
            update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
        elif command == "delete":
            if len(sys.argv) < 3:
                raise ValueError("Usage: delete <id>")
            delete_task(int(sys.argv[2]))
        elif command == "mark-in-progress":
            if len(sys.argv) < 3:
                raise ValueError("Usage: mark-in-progress <id>")
            mark_status(int(sys.argv[2]), "in-progress")
        elif command == "mark-done":
            if len(sys.argv) < 3:
                raise ValueError("Usage: mark-done <id>")
            mark_status(int(sys.argv[2]), "done")
        elif command == "list":
            if len(sys.argv) > 2:
                list_tasks(sys.argv[2])
            else:
                list_tasks()
        else:
            print(f"Unknown command: {command}")
    except ValueError as e:
        print(f"Error {e}")


def now():
    return datetime.now().isoformat()


def load_tasks_from_file():
    if not os.path.exists(TASKS_FILE):
        return {"tasks": []}
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: the task file is corrupted. It will be reset.")
        return {"tasks": []}


def format_date(iso_str):
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%d/%m/%Y %H:%M")
    except ValueError:
        return iso_str


def save_tasks_to_file(tasks_data):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks_data, file, indent=4)


def add_task(description):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    new_id = max([task["id"] for task in tasks], default=0) + 1
    new_task = {
        "id": new_id,
        "description": description,
        "status": "not done",
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
            try:
                save_tasks_to_file({"tasks": tasks})
                print(f"Task updated successfully (ID: {task_id})")
            except Exception as e:
                print(f"Task updated successfully (ID: {task_id})")
            return
    print(f"No task with ID {task_id} found.")


def delete_task(task_id):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    new_tasks = [task for task in tasks if task["id"] != task_id]
    if len(tasks) == len(new_tasks):
        print(f"No task with ID {task_id} found.")
    else:
        try:
            save_tasks_to_file({"tasks": new_tasks})
            print(f"Task {task_id} deleted.")
        except Exception as e:
            print(f"Error saving tasks: {e}")


def mark_status(task_id, status):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = now()
            try:
                save_tasks_to_file({"tasks": tasks})
                print(f"Task {task_id} marked as {status}.")
            except Exception as e:
                print(f"Error saving tasks: {e}")
            return
    print(f"No task with ID {task_id} found.")


def list_tasks(filter_status=None):
    tasks_data = load_tasks_from_file()
    tasks = tasks_data["tasks"]
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[ID: {task['id']}] [Status: {task['status']}]")
        print(f"  Description: {task['description']}")
        print(f"  Created:    {format_date(task['createdAt'])}")
        print(f"  Updated:    {format_date(task['updatedAt'])}")
        print()


if __name__ == "__main__":
    main()
