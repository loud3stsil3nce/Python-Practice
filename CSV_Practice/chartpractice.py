with open("CSV_Practice\employeedata.csv") as employee_data:
    employees = {}
    for line in employee_data:
        line = line.replace("\n", "")
        items = line.split(",")
        items.pop(0)
        employees[items[0]] = items[1:]
  #  print(employees)
    for person in employees:
        print(f"{person} is {employees[person][0]} years old, works as {employees[person][1]} and makes ${employees[person][2]} per year.")
    

