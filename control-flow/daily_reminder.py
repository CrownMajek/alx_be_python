task = input ("Enter your task: ")
priority = input("priority (high/medium/low: ")
time_bound = input("is it a time-bound? (yes or no: ")
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
        if time_bound == "yes":
            message +=" That requires immediate attention today!"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            message += " Please handle it soon."
    case "low":
        message = f"Remindeer: '{task}' is a low priority task."
        if time_bound == "yes":
            message += " No rush, but dont forget it."
    case _:
        message = f"Reminder: '{task}' is a task with unspecified priority"
print(message)