import itertools

# Tasks will be stored in a list; each task is a dictionary
sequence_counter = itertools.count(1)

tasks = [
    {
        "sequence_number": next(sequence_counter),
        "task_name": "Task 1",
        "status": "Completed"
    },
    {
        "sequence_number": next(sequence_counter),
        "task_name": "Task 2",
        "status": "Pending"
    },
    {
        "sequence_number": next(sequence_counter),
        "task_name": "Task 3",
        "status": "Deleted"
    }
]

# Add a new task
def add_task(task_name, status):
    status = status.capitalize()
    if status not in ["Completed", "Pending", "Deleted"]:
        print("Invalid status. Please use Completed, Pending, or Deleted.")
        return

    seq_num = next(sequence_counter)
    task = {
        "sequence_number": seq_num,
        "task_name": task_name,
        "status": status
    }
    tasks.append(task)
    print(f"Task number {seq_num}: '{task_name}' added with status '{status}'.")

# Complete a task
def complete_task(task_name):
    for task in tasks:
        if task["task_name"] == task_name and task["status"] == "Pending":
            task["status"] = "Completed"
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found or not pending.")

# Delete a task
def delete_task(task_name):
    for task in tasks:
        if task["task_name"] == task_name and task["status"] != "Deleted":
            task["status"] = "Deleted"
            tasks.remove(task)
            print(f"Task '{task_name}' marked as deleted.")
            return
    print(f"Task '{task_name}' not found or already deleted.")

# List completed tasks
def list_completed_tasks():
    completed_tasks = [task for task in tasks if task["status"] == "Completed"]
    if completed_tasks:
        print("Completed tasks:")
        for task in completed_tasks:
            print(f"Seq {task['sequence_number']}: {task['task_name']}")
    else:
        print("No completed tasks found.")

# List all tasks
def list_all_tasks():
    if tasks:
        print("All tasks:")
        for task in sorted(tasks, key=lambda t: t["sequence_number"]):
            print(f"Seq {task['sequence_number']}: {task['task_name']} [{task['status']}]")
    else:
        print("No tasks available.")

# Exit function
def exit_program():
    print("Exiting the program.")
    return False

# Main program loop
def main():
    while True:
        print("\nMenu:")
        print("1. Add a new task")
        print("2. Complete a task")
        print("3. Delete a task")
        print("4. List completed tasks")
        print("5. List all tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            status = input("Enter the status (Completed/Pending/Deleted): ")
            add_task(task_name, status)
        elif choice == "2":
            task_name = input("Enter the task name to mark as completed: ")
            complete_task(task_name)
        elif choice == "3":
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif choice == "4":
            list_completed_tasks()
        elif choice == "5":
            list_all_tasks()
        elif choice == "6":
            if not exit_program():
                break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()
