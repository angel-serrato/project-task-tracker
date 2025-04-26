# Task CLI - Command Line To-Do App

A simple command-line task manager written in Python.  
Add, update, delete, and list your tasks directly from the terminal. Tasks are stored locally in a JSON file.

![taskcli](https://github.com/user-attachments/assets/1927faf7-75af-4cd3-b1b2-f9d3052ea10c)

## Features

- Add tasks with descriptions
- Update task descriptions
- Delete task by ID
- Mark task as "in-progress" or "done"
- List all tasks or filter by status (done, not done, in-progress)
- Automatically creates "tasks.json" if it doesn’t exist
- No external libraries required (pure Python)

## Requirements

- Python 3.13
- No external dependencies (uses Python standard library)

## Usage

Run the script from the terminal:

    python task_cli.py <command> [options]

### Available Commands:

- **add**  
  Example: `python task_cli.py add Buy groceries` 
  Adds a new task.

- **update**  
  Example: `python task_cli.py update 1 New description`  
  Updates the description of a task.

- **delete**  
  Example: `python task_cli.py delete 1`  
  Deletes a task by ID.

- **mark-in-progress**  
  Example: `python task_cli.py mark-in-progress 2`  
  Marks a task as in-progress.

- **mark-done**  
  Example: `python task_cli.py mark-done 2`  
  Marks a task as done.

- **list**  
  Example: `python task_cli.py list`  
  Lists all tasks.

- **list done**  
  Example: `python task_cli.py list done`  
  Lists tasks marked as done.

- **list not done**  
  Example: `python task_cli.py list not done`  
  Lists tasks that are not done.

- **list in-progress**  
  Example: `python task_cli.py list in-progress`  
  Lists tasks marked as in-progress.

## File Structure

- **task_cli.py** - Main script
- **tasks.json** - JSON file used to store tasks

## Error Handling

- Invalid commands or missing arguments show error messages.
- If the tasks.json file is corrupted, it resets automatically.
- Invalid or non-existent task IDs are handled cleanly.

## Git Ignore Suggestion

To avoid committing local task data, add this line to your `.gitignore` file:

    tasks.json

## Example Output

    $ python task_cli.py add "Finish writing report"
    Task added successfully (ID: 1)

    $ python task_cli.py list
    [ID: 1] [Status: not done]
      Description: Finish writing report
      Created:    25/04/2025 18:00
      Updated:    25/04/2025 18:00

## License

This project is open-source and free to use.
