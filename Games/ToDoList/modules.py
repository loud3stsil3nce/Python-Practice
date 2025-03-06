from pathlib import Path

taskname = ''
description = ''
ToDo = []
task = {}
num = len(ToDo)



def menu():
    try:
        action = int(input("What would you like to do?\n1)View tasks\n2)Add Tasks\n3)Remove Tasks:\n"))
    except ValueError:
        action = int(input("Please type in a valid number:\n1)View tasks\n2)Add Tasks\n3)Remove Tasks:\n"))
    return action
def asktask():
    global taskname
    taskname = input("What is the name of your new task?\n")
    return taskname

def askdescription():
    global description
    description = input("Description of task (press enter if N/A):\n")
    return description

def addtask(name, description):
    global ToDo
    task = {}
    task[f"{name}"] = description
    ToDo.append(task)
    todofile = Path(__file__).parent / "todo.txt"
    with open(todofile, "a") as todofile:    
        todofile.write(f"{len(ToDo)}. {name}: \n{description}\n")
    todofile.close()

def viewalltasks():
    
    if len(ToDo) == 0:
        print("No tasks found")
    else:
        for task in ToDo:
            for key, value in task.items():
                print(f"{ToDo.index(task) + 1}. {key}:\n{value}\n")
     
       

def remove(taskkey):
    global ToDo
    ToDo.pop(taskkey - 1)
         
    todofile = Path(__file__).parent / "todo.txt"
    with open(todofile, "w") as todofile:  
        for task in ToDo:
            for key, value in task.items():
                todofile.write(f"{ToDo.index(task) + 1}. {key}:\n{value}\n")
    todofile.close()
      