from faker import Faker
fake = Faker()
location = fake.city()
age = 0
balance = 0
employed = False
employer = "N/A"
alive = True


Menu = {
    1: "Proceed",
    2: "Stats",
    3: "Family",
    4: "Actions"
    
    }


def Provide_Menu():
    choice = (input(f"- - - - - - - - - -\nPlease make a choice:\nMenu:\n1: {Menu[1]}\n2: {Menu[2]}\n3: {Menu[3]}\n4: {Menu[4]}\nChoice: "))
    if not choice.isdigit():
        while not choice.isdigit():
            choice = (input(f"- - - - - - - - - -\nPlease make a valid number choice:\nMenu:\n1: {Menu[1]}\n2: {Menu[2]}\n3: {Menu[3]}\n4: {Menu[4]}\nChoice: "))
    
    choice = int(choice)
    
    return choice
def Continue(choice: int):
    print("\n\n\n")
    if choice == 1:
        global age
        age += 1
        print(f"Your age now: {age}\n")
    if choice == 2:
        pass
        
        #global name, location, age, balance, employed, employer
        
        
        print(f"{name}'s stats:\nLocation: {location}\nCurrent Age: {age}\nBalance: ${balance}")
        if employed == True:
            print(f"Current employer: {employer}")
        else:
            print("Currently unemployed.")
        
    if choice == 3:
        pass
    if choice == 4:
        print("works")
    
    
name = str(input("Please type your name: "))
def main():
    
    
    
    print(f"Welcome to the Game of Life, {name}. \nPrepare to embark on this wild journey full of events, lessons, victory, defeat, and memories. \nYou are currently {age} years old. \nYou are located in {location}.")
   # Provide_Menu()
    while alive == True:
        
        Continue(Provide_Menu())
        
    
main()