task = input("Enter your task: ")
time_bound = input("Is it time-bound?(yes/no): ")
priority = input("Priority (high/medium/low): ")
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' is a task with unspecified priority")