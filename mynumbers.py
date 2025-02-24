with open("numbers.txt") as my_numbers:
    
    numList= []
    def largest():
        for number in my_numbers:
            number = number.replace("\n", "")
            numList.append(int(number))
        ordered = sorted(numList)
        return ordered[-1]
    


    print(largest())
    
