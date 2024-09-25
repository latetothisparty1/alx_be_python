# daily_reminder.py

# Step 1: Prompt for a single task, priority, and time-bound status
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # converting to lowercase for consistency
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process the task based on priority using Match Case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Step 3: Modify reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += "."

# Step 4: Provide the customized reminder
print("\nReminder:", reminder)
