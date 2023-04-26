# iCaly Task Scheduler

iCaly is a task scheduler tool that helps you manage your daily tasks and create an optimized schedule based on task priorities and due dates. It takes a CSV file containing task names, priorities, due dates and durations and outputs an iCalendar (.ics) file that can be imported into most calendar applications.

## Installation

1. Clone the repository to your local machine.
   ```
   git clone https://github.com/your-username/icaly-task-scheduler.git
   ```
2. Navigate to the project directory.
   ```
   cd icaly-task-scheduler
   ```
3. Install the required packages using pip.
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a CSV file named `tasks.csv` with columns for task name, priority, and duration in hours. For example:

   ```
Task,Duration,Due Date,Priority
Programming Week 8 Notes,1.5,2023-05-01,1
Programming Week 8 Labs,1,2023-05-01,2
   ```

   Note: If a task's duration exceeds the remaining time in the day, it will not be included in the schedule. The tool assumes that tasks can be scheduled from 9:00 AM to 11:00 PM. Tasks are sorted by due date and priority, with higher priority tasks taking precedence.

2. Run the script `icaly.py`.
   ```
   python icaly.py
   ```
3. The tool will output an iCalendar file named `schedule.ics` in the project directory.
4. Import the iCalendar file into your preferred calendar application by selecting "Import Calendar" and selecting the file.

## Example Output

## Contributions

Contributions to the iCaly Task Scheduler project are always welcome! If you find a bug or have a suggestion for a new feature, please open an issue on the GitHub repository or create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
