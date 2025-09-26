Task = input ("Enter your task: ")
Priority = input("Priority (high/medium/low: ")
Time_bound = input("Is it a time-bound? (yes/no): ")
match Priority:
    case "high":
        message = f"Reminder: '{Task}' is a high priority task."
        if Time_bound == "yes":
            message +=" That requires immediate attention today!"
    case "medium":
        message = f"Reminder: '{Task}' is a medium priority task."
        if Time_bound == "yes":
            message += " Please handle it soon."
    case "low":
        message = f"Remindeer: '{Task}' is a low priority task."
        if Time_bound == "yes":
            message += " No rush, but dont forget it."
    case _:
        message = f"Reminder: '{Task}' is a task with unspecified priority"
print(message)