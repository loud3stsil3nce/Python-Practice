from pathlib import Path
import modules
menu = modules.menu
viewalltasks = modules.viewalltasks
addtask = modules.addtask
asktask = modules.asktask
askdescription = modules.askdescription
remove = modules.remove

def main():
    while True:
        action = menu() 
        if action == 1:
            viewalltasks()
        if action == 2:
            addtask(asktask(), askdescription())
        if action == 3:
            try:
                removedTask = int(input("Type the number of the task you'd like to remove:\n"))
            except ValueError:
                removedTask = int(input("Please type in a valid number for the task you'd like to remove:\n"))
            remove(removedTask)
main()