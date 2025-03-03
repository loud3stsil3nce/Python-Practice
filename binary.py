#******************************************************************************
# binary.py
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

import random

# The two lines below set the random seed for testing on Gradescope. Comment out these lines to test your code on Spyder.
#####################
#seed = input() # comment out to test on Spyder, but leave for Gradescope submission
#random.seed(seed) # comment out to test on Spyder, but leave for Gradescope submission
#####################

# YOUR CODE SHOULD START BELOW. THE LINES ABOVE NEED TO BE BEFORE YOUR CODE! #

eights = int(input("Enter 8's digit: "))
fours = int(input("Enter 4's digit: "))
twos = int(input("Enter 2's digit: "))
ones = int(input("Enter 1's digit: "))


num = random.randrange(0,16)
binary = (f"{str(eights)}{str(fours)}{str(twos)}{str(ones)}")
total = (8*eights) + (4*fours) + (2*twos) + (1*ones)

print(f"The binary number {binary} is {total} in base ten")
if total < num:
    print(f"Less than the randomly generated number {num}? True")
else:
    print(f"Less than the randomly generated number {num}? False")

