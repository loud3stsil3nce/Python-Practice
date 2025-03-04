from pathlib import Path
taskname = ''
description = ''
ToDo = []
task = {}


def menu():
    try:
        action = int(input("What would you like to do?\n1)View tasks\n2)Add Tasks\n3)Remove Tasks\n: "))
    except ValueError:
        action = int(input("Please type in a valid number:\n1)View tasks\n2)Add Tasks\n3)Remove Tasks\n: "))
    return action
def asktask():
    global taskname
    taskname = input("What is the name of your new task? ")
    return taskname

def askdescription():
    global description
    description = input("Description of task (press enter if N/A) ")
    return description

def addtask(name, description):
    global task
    task[name] = description
    todofile = Path(__file__).parent / "todo.txt"
    with open(todofile, "a") as todofile:    
        todofile.write(f"Task: {name} Description: {description}\n")

def viewalltasks():
    todofile = Path(__file__).parent / "todo.txt"
    with open(todofile) as todofile:    

        len = 0
        for line in todofile:
            print(line)
        
            len += 1 
        print(task)
        if len == 0:
            print("No tasks found")

def remove(taskkey):
    pass        
                 
    
def main():
    while True:
        action = menu() 
        if action == 1:
            viewalltasks()
        if action == 2:
            addtask(asktask(), askdescription())
        if action == 3:
            pass
main()