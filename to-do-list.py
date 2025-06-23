# simple_todo.py

todo_list = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not todo_list:
            print("No tasks yet.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter task to add: ")
        todo_list.append(task)
        print("Task added!")

    elif choice == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
