with open("practice.csv") as csv_file:
    def read_file():
        dictionary = {}
        for line in csv_file:
            line = line.replace("\n", "")
            content = line.split(",")
        #for line in csv_file:
            name = content[0]
            age = content[1]
            dictionary[name] = age
    #    print(dictionary)
        dictionary.pop('Name')
        print(dictionary)
        print(f"Format:\n---\nName: Age\n---------")    
        for person in dictionary:
            print(f"{person}: {dictionary[person]}")
       #     print(dictionary[person])
            print( )



    read_file()
