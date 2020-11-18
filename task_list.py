tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# As a user, to manage my task list I would like a program that allows me to:

# Print a list of uncompleted tasks - filter by true or false
# for task in tasks:
#     if task["completed"] == False:
#         print(task)

def uncompleted(tasks):
    uncompleted = []
    for task in tasks:
        if task["completed"] == False:
            uncompleted.append(task)
    return uncompleted

print(uncompleted(tasks))

# Print a list of completed tasks - filter by true or false

def completed(tasks):
    uncompleted = []
    for task in tasks:
        if task["completed"] == True:
            uncompleted.append(task)
    return uncompleted

print("Completed")
print(completed(tasks))

# for task in tasks:
#     if task["completed"] == True:
#         print(task)

# Print a list of all task descriptions - 

# for task in tasks:
#     print (task["description"])

# Print a list of tasks where time_taken is at least a given time - print (if time_taken >= 0)

# for task in tasks:
#     if task["time_taken"] < 20:
#         print(task)

# Print any task with a given description 

for task in tasks:
    if task["description"] == 'Wash Dishes':
        print(task)