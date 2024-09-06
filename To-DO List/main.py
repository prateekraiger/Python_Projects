class ToDoList:
    def __init__(self):
        self.tasks = {}

    def create_task(self, tsk_nm):
        """Create a new task"""
        if tsk_nm not in self.tasks:
            self.tasks[tsk_nm] = False
            print(f"Task '{tsk_nm}' created successfully.")
        else:
            print(f"Task '{tsk_nm}' already exists.")

    def view_tasks(self):
        """View all tasks"""
        if not self.tasks:
            print("No tasks available.")
        else:
            for task, status in self.tasks.items():
                status = "Completed" if status else "Not Completed"
                print(f"Task: {task}, Status: {status}")

    def update_task(self, tsk_nm, new_tsk_nm):
        """Update an existing task"""
        if tsk_nm in self.tasks:
            self.tasks[new_tsk_nm] = self.tasks.pop(tsk_nm)
            print(f"Task '{tsk_nm}' updated to '{new_tsk_nm}' successfully.")
        else:
            print(f"Task '{tsk_nm}' not found.")

    def delete_task(self, tsk_nm):
        """Delete a task"""
        if tsk_nm in self.tasks:
            del self.tasks[tsk_nm]
            print(f"Task '{tsk_nm}' deleted successfully.")
        else:
            print(f"Task '{tsk_nm}' not found.")

    def is_comp(self, tsk_nm):
        """Mark a task as completed"""
        if tsk_nm in self.tasks:
            self.tasks[tsk_nm] = True
            print(f"Task '{tsk_nm}' marked as completed.")
        else:
            print(f"Task '{tsk_nm}' not found.")


def main():
    todo = ToDoList()

    while True:
        print("\n1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            tsk_nm = input("Enter task name: ")
            todo.create_task(tsk_nm)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            tsk_nm = input("Enter task name: ")
            new_tsk_nm = input("Enter new task name: ")
            todo.update_task(tsk_nm, new_tsk_nm)
        elif choice == "4":
            tsk_nm = input("Enter task name: ")
            todo.delete_task(tsk_nm)
        elif choice == "5":
            tsk_nm = input("Enter task name: ")
            todo.is_comp(tsk_nm)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()