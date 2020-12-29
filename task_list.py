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



# Print any task with a given description 

def contains_given_desc(tasks, desc):
    for task in tasks:
        if task["description"] == desc:
            print(task)
print("TASK WITH GIVEN DESC")
contains_given_desc(tasks, "Clean Windows")
contains_given_desc(tasks, "Feed Cat")
contains_given_desc(tasks, "Make Dinner")

# Extension
# Given a description update that task to mark it as complete.
def mark_as_completed(tasks, desc):
    for task in tasks:
        if task["description"] == desc:
            task["completed"] = True

mark_as_completed(tasks, "Feed Cat")
print("MARK AS COMPLETED")
mark_as_completed(tasks, "Wash Dishes")
print(tasks)
