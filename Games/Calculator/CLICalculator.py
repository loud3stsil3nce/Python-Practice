# importing functions for add, subtract, divide, multiply, power, and root
import Modules
add = Modules.add
subtract = Modules.subtract
multiply = Modules.multiply
divide = Modules.divide
power = Modules.power
squareRoot = Modules.squareRoot

def main():
    while True: # error handling

        try:
            firstValue = int(input("First number of operation: "))
            userOperation = input("Operation (+, -, /, *, **, sqrt): ")
            secondValue = int(input("Second number of operation: "))
            if userOperation == '+':
                total = add(firstValue, secondValue)
                print(total)
            elif userOperation == '-':
                total = subtract(firstValue, secondValue)
                print(total)
            elif userOperation == '/':
                total = divide(firstValue, secondValue)
                print(total)
            elif userOperation == '*':
                total = multiply(firstValue, secondValue)
                print(total)
            elif userOperation == '**':
                total = power(firstValue, secondValue)
                print(total)
            elif userOperation == 'sqrt':
                total = squareRoot(firstValue, secondValue)
                print(total)
            else: # user inputs operation or character not supported
                print("Invalid operation")
        except ValueError: # if user inputs a non-number character
            "Please type in a valud number"

main()