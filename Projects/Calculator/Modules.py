import math



def add(firstValue, secondValue):
    sum = firstValue + secondValue
    return sum

def subtract(firstValue, secondValue):
    difference = firstValue - secondValue
    return difference

def multiply(firstValue, secondValue):
    product = firstValue * secondValue
    return product

def divide(firstValue, secondValue):
    quotient = firstValue / secondValue
    return quotient

def power(firstValue, secondValue):
    power = firstValue ** secondValue
    return power 

def squareRoot(firstValue, secondValue):
    squareRoot = math.pow(firstValue, 1/secondValue)
    return squareRoot