task=input("Enter the task description: ")
priority=input("Enter the task priority(high/medium/low): ")
time_bound=input("Is the task time bound(yes/no): ")
match priority:
  case"high":
      if time_bound=="yes":
       print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
      else:
       print("Reminder: 'Finish project report' is a high priority task that requires attention soon!")

  case"low":
      if time_bound=="yes":
          print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
      else:
          print("Note: 'Read a book' is a low priority task.")
  case"medium":
      if time_bound=="yes":
          print("This task is  a medium task do it when you find time")
      else:
          print("This task is  a medium task but find time to do it")

