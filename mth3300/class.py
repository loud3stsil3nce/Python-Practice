n = input('Enter name: ')

with open("practice.txt", "a") as file:
    file.write(f"Hello my name is {n}\n")