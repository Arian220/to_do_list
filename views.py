class TaskView:
    """
    Manages the user interface for the terminal-based to-do list application.

    Attributes:
        controller (TaskController): The controller responsible for managing tasks.
    
    Methods:
        show_menu(): Displays the main menu options to the user.
        get_user_choice(): Prompts the user to select an option from the menu.
        add_task(): Prompts the user to input details for a new task and adds it.
        remove_task(): Displays the list of tasks and prompts the user to choose one to remove.
        show_tasks(): Displays all current tasks to the user.
        start(): Starts the user interface loop, allowing the user to interact with tasks.
    """

    def __init__(self, controller):
        """
        Initializes the TaskView with the provided controller.

        Args:
            controller (TaskController): The controller responsible for managing tasks.
        """
        self.controller = controller

    def show_menu(self):
        """
        Displays the main menu options to the user.
        """
        print("=== Task List Menu ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

    def get_user_choice(self):
        """
        Prompts the user to select an option from the menu.

        Returns:
            str: The user's choice as a string.
        """
        choice = input("Choose an option: ")
        return choice

    def add_task(self):
        """
        Prompts the user to input details for a new task and adds it using the controller.
        """
        name = input("Task Name: ")
        print("Available task types:")
        for i, t in enumerate(self.controller.get_task_types()):
            print(f"{i + 1}. {t.name}")
        task_type = input("Choose the task type: ")
        date_str = input("Date (YYYY-MM-DD): ")
        urgency = input("Urgency (High, Medium, Low): ")
        
        selected_task_type = self.controller.get_task_types()[int(task_type) - 1].name
        self.controller.add_task(name, selected_task_type, date_str, urgency)

    def remove_task(self):
        """
        Displays the list of tasks and prompts the user to choose one to remove.
        """
        tasks = self.controller.get_tasks()
        self.show_tasks()
        if tasks:
            index = int(input("Choose the number of the task to remove: ")) - 1
            self.controller.remove_task(index)

    def show_tasks(self):
        """
        Displays all current tasks to the user.
        """
        tasks = self.controller.get_tasks()
        if tasks:
            print("\n=== Tasks ===")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task.name} - {task.task_type} - {task.date.strftime('%Y-%m-%d')} - {task.urgency} ({task.color})")
            print()
        else:
            print("No tasks available.")

    def start(self):
        """
        Starts the user interface loop, allowing the user to interact with tasks.
        """
        while True:
            self.show_menu()
            choice = self.get_user_choice()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.remove_task()
            elif choice == '3':
                self.show_tasks()
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
