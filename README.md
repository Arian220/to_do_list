# Terminal-Based To-Do List Application

This is a terminal-based to-do list application written in Python. It allows users to manage tasks through a command-line interface, supporting task addition, removal, and viewing.

## Overview

The application is designed to manage tasks with attributes such as name, type, due date, and urgency level. Tasks are stored in a CSV file and can be added, removed, or viewed through a simple terminal interface.

## Features

- **Add Tasks:** Users can add new tasks with details such as name, type, due date, and urgency level.
- **Remove Tasks:** Users can remove existing tasks by selecting them from a list.
- **View Tasks:** Users can view a list of all current tasks with their details.

## File Structure

- `main.py`: Entry point for the application. Initializes the controller and view, then starts the application.
- `models.py`: Contains the `Task` and `TaskType` classes, defining the structure of tasks and their types.
- `views.py`: Manages the user interface and interaction logic for the terminal-based application.
- `controllers.py`: Contains the `TaskController` class that handles the business logic, including task management and storage.
- `storage.py`: Manages saving and loading tasks to and from a CSV file.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Arian220/to_do_list.git
    ```

2. Navigate to the project directory:
    ```bash
    cd to_do_list
    ```

3. Ensure you have Python 3 installed.

## Usage

1. Run the application:
    ```bash
    python main.py
    ```

2. Follow the prompts to add, remove, or view tasks.

## Classes

### `Task`
Represents a task with attributes like name, type, due date, and urgency level.

- **Attributes:**
  - `name` (str)
  - `task_type` (str)
  - `date` (datetime)
  - `urgency` (str)
  - `color` (str)

### `TaskController`
Handles the business logic for task management, including adding, removing, and retrieving tasks.

### `TaskView`
Provides the terminal-based user interface for interacting with the application.

### `TaskStorage`
Manages saving tasks to and loading tasks from a CSV file.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a branch for your changes (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push your branch (`git push origin feature/your-feature`).
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please contact [hernandezarian320@gmail.com].
