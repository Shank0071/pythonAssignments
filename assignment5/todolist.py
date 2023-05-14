tasks = []

def add_task():
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print("Task added successfully.")

def view_tasks():
    if tasks:
        for i, task in enumerate(tasks):
            status = 'Completed' if task['completed'] else 'Incomplete'
            print(f"{i+1}. {task['task']} - {status}")
    else:
        print("No tasks found.")

def mark_task():
    task_index = int(input("Enter the task number: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        tasks[task_index]['completed'] = True
        print("Task marked as completed.")

def delete_task():
    task_index = int(input("Enter the task number: ")) - 1
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task number.")
    else:
        del tasks[task_index]
        print("Task deleted successfully.")

while True:
    print("\n---- To-Do List Menu ----")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
