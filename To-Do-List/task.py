def main():
    tasks = []

    while True:
        print("\n====== To-Do-List ======")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Mark Task as Done")
        print("6. Exit")
        print("========================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print()
            task = input("Enter Task: ")
            tasks.append({"task": task, "Done" : False})
            print("Task Added Successfully")
        elif choice == '2':
            if not tasks:
                print("No tasks to edit!")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['task']}")
                
                try:
                    task_num = int(input("Enter task number to edit: ")) - 1
                    if 0 <= task_num < len(tasks):
                        new_task = input("Enter new task description: ")
                        tasks[task_num]['task'] = new_task
                        print("Task edited successfully!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Invalid input! Please enter a number.")
        elif choice == '3':
            if not tasks:
                print("No tasks to delete!")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['task']}")
                
                try:
                    task_num = int(input("Enter task number to delete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        deleted_task = tasks.pop(task_num)
                        print(f"Task '{deleted_task['task']}' deleted successfully!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Error: Please enter a valid number!")
        elif choice == '4':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "✓" if task["Done"] else "✗"
                print(f"{index + 1}. [{status}] {task['task']}")

        elif choice == '5':
            if not tasks:
                print("No tasks to mark!")
            else:
                print("\nTasks:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task['task']}")
                
                try:
                    task_num = int(input("Enter task number to mark as done: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["Done"] = True
                        print("Task marked as done! ✅")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Error: Please enter a number!")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")



if __name__ == "__main__":
    main()

