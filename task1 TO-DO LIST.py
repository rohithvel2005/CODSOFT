

class TodoApp:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("\n------ To-Do List Application ------")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Completed")
        print("6. Exit")
        print("--------------------------------------")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "[Completed]" if task['completed'] else "[Pending]"
                print(f"{i}. {task['title']} {status}")

    def add_task(self):
        title = input("\nEnter the task title: ").strip()
        if title:
            self.tasks.append({"title": title, "completed": False})
            print(f"Task '{title}' added successfully.")
        else:
            print("Task title cannot be empty.")

    def update_task(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to update: "))
            if 1 <= task_number <= len(self.tasks):
                new_title = input("Enter the new title for the task: ").strip()
                if new_title:
                    self.tasks[task_number - 1]['title'] = new_title
                    print("Task updated successfully.")
                else:
                    print("Task title cannot be empty.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(self.tasks):
                deleted_task = self.tasks.pop(task_number - 1)
                print(f"Task '{deleted_task['title']}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def mark_task_completed(self):
        self.view_tasks()
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(self.tasks):
                self.tasks[task_number - 1]['completed'] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def run(self):
        while True:
            print("=====================================")
            
            self.display_menu()
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.view_tasks()
                elif choice == 2:
                    self.add_task()
                elif choice == 3:
                    self.update_task()
                elif choice == 4:
                    self.delete_task()
                elif choice == 5:
                    self.mark_task_completed()
                elif choice == 6:
                    print("\nExiting the application. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
