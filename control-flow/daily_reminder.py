# daily_reminder.py

# Get user input
task = input("Enter the task description: ")
priority = input("Enter the task priority (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Use match-case to determine the message
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be completed soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to schedule it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but it's time-bound. Consider doing it today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
