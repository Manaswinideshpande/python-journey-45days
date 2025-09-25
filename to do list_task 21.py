class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print("Task removed successfully!")
                return
        print("Task not found in the list.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print("Task marked as completed!")
                return
        print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, t in enumerate(self.tasks, start=1):
                status = "Completed" if t["completed"] else "Not Completed"
                print(f"{i}. {t['task']} - {status}")
        else:
            print("No tasks in the list.")

def main():
    todo_list = TodoList()
    
    while True:
        print("\nTODO LIST MENU:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
main()
