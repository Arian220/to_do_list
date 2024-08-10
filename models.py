from datetime import datetime

class Task:
    """
    Represents a task in the to-do list.

    Attributes:
        name (str): The name or description of the task.
        task_type (str): The category or type of the task (e.g., "School", "Personal").
        date (datetime): The due date of the task.
        urgency (str): The urgency level of the task (e.g., "High", "Medium", "Low").
        color (str): The color associated with the urgency level of the task.
    
    Methods:
        set_color(): Sets the color based on the urgency level of the task.
    """
    def __init__(self, name, task_type, date, urgency):
        """
        Initializes a Task object with the provided name, task type, date, and urgency level.

        Args:
            name (str): The name or description of the task.
            task_type (str): The type of the task.
            date (datetime): The due date of the task.
            urgency (str): The urgency level of the task.
        """
        self.name = name
        self.task_type = task_type
        self.date = date
        self.urgency = urgency
        self.color = self.set_color()

    def set_color(self):
        """
        Determines and returns the color based on the urgency level.

        Returns:
            str: The color associated with the urgency level.
                - 'Red' for 'High' urgency.
                - 'Yellow' for 'Medium' urgency.
                - 'Green' for 'Low' urgency.
                - 'Blue' for any other urgency level.
        """
        if self.urgency == 'High':
            return 'Red'
        elif self.urgency == 'Medium':
            return 'Yellow'
        elif self.urgency == 'Low':
            return 'Green'
        else:
            return 'Blue'

class TaskType:
    """
    Represents a type or category of task.

    Attributes:
        name (str): The name of the task type.
    """
    def __init__(self, name):
        """
        Initializes a TaskType object with the provided name.

        Args:
            name (str): The name of the task type.
        """
        self.name = name

# A list of predefined task types.
task_types = [
    TaskType("School"),
    TaskType("Personal"),
    TaskType("Partner"),
    TaskType("Sport")
]
