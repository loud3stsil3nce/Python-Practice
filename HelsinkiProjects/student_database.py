# Write your solution here


def add_student(students: dict, name: str):
    pass
    if name not in students:
        students[name] = []
        

def print_student(students: dict, searchname: str):
    totalgrade = 0
    numberofclasses = 0
    if searchname not in students:
        print(f"{searchname}: no such person in the database")
        return
    if students[searchname] == []:
        print(f"{searchname}:\n no completed courses")
    else: 
        print(f"{searchname}:\n {len(students[searchname])} completed courses:")
        for each in students[searchname]:
            print(f"  {each[0]} {each[1]}")
            totalgrade += each[1]
            numberofclasses += 1
        average = totalgrade / numberofclasses
        print(f" average grade {average}")

def add_course(students: dict, studentname: str, courseinfo: tuple):
    if courseinfo[1] == 0:
        return
    
    
    for key, value in students[studentname]:        
      
        if courseinfo[0] == key:
            if value > courseinfo[1]:
                return
            elif value < courseinfo[1]:
                for classes in students[studentname]:
                    if courseinfo[0] in classes:
                        students[studentname].remove(classes)                                   
    else:
        students[studentname].append(courseinfo)
        
def summary(students: dict):
    population = 0
    for student in students:
        population += 1
    
    courseload = 0
    for student in students:
        if len(students[student]) > courseload:
            courseload = len(students[student])
           
    for student in students:
        if len(students[student]) == courseload:
            winner = student
            
    highestgrade = 0
    for student in students:
        gradesum = 0
        classes = 0
        
        for each in students[student]:
            gradesum += each[1]
            classes += 1
        if gradesum / classes > highestgrade:
            highestgrade = gradesum / classes
            gpawinner = student
       
    print(f"students {population}\nmost courses completed {courseload} {winner}\nbest average grade {highestgrade} {gpawinner}")
    
