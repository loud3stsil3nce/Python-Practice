import random
max =  (input("Please pick a maximum number to set the mystery number at: ")) # sets max random number
#if type(max) != int:      #if the user input is not an integer, repeat prompt until fulfills criteria
if not max.isdigit():
    while not max.isdigit():
        max = (input("Please pick an INTEGER to set the maximum possible mystery number at: "))
max = int(max)
n = random.randint(1,max)  
tries = 0   #counts user attempts

def distance(n, guess):
    dist = abs(n - guess)
    return dist

guess = int(input("Please try to guess the number: "))
dist = distance(n, guess)
tries += 1
while guess != n:
    if guess < n:
        if tries >= 2:
            if distance(n, guess) > dist:
                print("Colder...")
            elif distance(n, guess) < dist:
                print("Hotter!")
            else:
                print("Same temp.")
            
            
        guess = int(input(f"Try again... (hint: go higher!): "))
        tries += 1
    elif guess > n:
        if tries >= 2:
            if distance(n, guess) > dist:
                print("Colder...")
            elif distance(n, guess) < dist:
                print("Hotter!")
            else:
                print("Same temp.")
        
        guess = int(input(f"Try again... (hint: go lower!): "))
        tries += 1
if tries == 1:
    print(f"Correct!\nIt took you {tries} try to guess the number. You guessed {guess}, and \"guess\" what? The secret number is {n} ")
else:
    print(f"Correct!\nIt took you {tries} tries to guess the number. You guessed {guess}, and \"guess\" what? The secret number is {n} ")


