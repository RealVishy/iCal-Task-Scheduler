import csv
from datetime import datetime, timedelta
from icalendar import Calendar, Event

def load_tasks(file_path):
    """
    Load tasks from CSV file.
    """
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        return [{'name': row[0], 'duration': float(row[1]),
                 'due_date': datetime.strptime(row[2], '%Y-%m-%d'),
                 'priority': int(row[3])} for row in reader]

def main():
    tasks = sorted(load_tasks('tasks.csv'), key=lambda t: (t['due_date'], -t['priority']))
    now = datetime.now()
    current_time = now if now.hour >= 9 else now.replace(hour=9, minute=0, second=0, microsecond=0)
    end_time = current_time.replace(hour=23, minute=0, second=0, microsecond=0)
    remaining_time = (end_time - current_time).total_seconds() / 3600
    schedule, cal = [], Calendar()

    for task in tasks:
        if task['duration'] <= remaining_time:
            schedule.append(task)
            remaining_time -= task['duration']
            event = Event()
            event.add('summary', task['name'])
            event.add('dtstart', current_time)
            event.add('dtend', current_time + timedelta(hours=task['duration']))
            event.add('priority', task['priority'])
            cal.add_component(event)
            current_time += timedelta(hours=task['duration'])

    print('Schedule:')
    for i, task in enumerate(schedule):
        start_time = (current_time - timedelta(hours=task['duration'])).strftime('%I:%M %p')
        end_time = current_time.strftime('%I:%M %p')
        print(f"{i+1}. {task['name']} ({task['duration']} hours) from {start_time} to {end_time}")

    with open('schedule.ics', 'wb') as f:
        f.write(cal.to_ical())

if __name__ == "__main__":
    main()
