import json
import os
import sys

TASKS_FILE = 'tasks.json'

"""
Cargar tareas desde el archivo JSON
"""
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return {"tasks": []}
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)

def list_tasks():
    tasks_data = load_tasks()
    tasks = tasks_data['tasks']
    for task in tasks:
        print(f"ID: {task['id']} | Description: {task['description']}")

""" 
Guardar tareas en el archivo JSON 
"""
def save_tasks(tasks_data):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks_data, file, indent=4)

def add_task(description):
    tasks_data = load_tasks()
    new_task = {
        "id": len(tasks_data["tasks"]) + 1,
        "description": description,
    }
    tasks_data["tasks"].append(new_task)
    save_tasks(tasks_data)
    print("Task added")

def main():
    if len(sys.argv) < 2:
        print("Usage: task_cli.py <command> [options]")
        return
    command = sys.argv[1]
    if command == 'add' and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        if len(sys.argv) > 2:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Unknown command or missing arguments.")

if __name__ == '__main__':
    main()