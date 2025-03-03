#******************************************************************************
# parking.py
#******************************************************************************
# Name: Rafiur Rahman
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# NONE
# NONE
# NONE
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

car1 = int(input("Car 1 preferred spot: "))
car2 = int(input("Car 2 preferred spot: "))

if car1 == car2:
    if car1 == 3:
        print(f"Car 1 parks in spot {car1}")
        print("Car 2 cannot park")
    else:
        print(f"Car 1 parks in spot {car1}\nCar 2 parks in spot {car1 + 1}")
        
else:
    print(f"Car 1 parks in spot {car1}\nCar 2 parks in spot {car2}")

    

