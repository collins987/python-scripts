todo_file = "todo.txt"

def add_task(task):
    with open(todo_file, "a") as f:
        f.write(task + "\n")

def list_tasks():
    with open(todo_file, "r") as f:
        return f.readlines()

def remove_task(task):
    tasks = list_tasks()
    with open(todo_file, "w") as f:
        for t in tasks:
            if t.strip() != task:
                f.write(t)

def main():
    while True:
        print("\nWelcome: To-Do List Application")
        print("1. Add a new task")
        print("2. View tasks not yet completed")
        print("3. Remove tasks in list")
        print("4. Exit to do list application")
        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter a task: ")
            add_task(task)
            print(f"Task '{task}' has been added successfully.")
        elif choice == "2":
            tasks = list_tasks()
            print("\nTasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task.strip()}")
        elif choice == "3":
            task = input("Enter a task to remove: ")
            remove_task(task)
            print(f"Task '{task}' removed.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
