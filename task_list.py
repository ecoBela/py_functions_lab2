tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#Print a list of uncompleted tasks
def uncompleted_tasks(tasks):
    uncompleted = []
    for task in tasks:
        if task["completed"] == False:
            uncompleted.append(task)
            print(task["description"])
    print(uncompleted)

uncompleted_tasks(tasks)

# Print a list of completed tasks -

def completed(tasks):
    completed = []
    for task in tasks:
        if task["completed"] == True:
            completed.append(task)
            print(task["description"])
    return completed

print("Completed")
completed(tasks)


# Print a list of all task descriptions - 

def task_descriptions(tasks):
    for task in tasks:
        print(task["description"])

print("TASK DESCRIPTIONS")
task_descriptions(tasks)

# Print a list of tasks where time_taken is at least a given time - print (if time_taken >= 0)
def time_taken(tasks, time):
    for task in tasks:
        if task["time_taken"] > time:
            print(task)

print("TIME TAKEN TASKS")
time_taken(tasks, 20)

# for task in tasks:
#     if task["time_taken"] < 20:
#         print(task)

# Print any task with a given description 

# for task in tasks:
#     if task["description"] == 'Wash Dishes':
#         print(task)