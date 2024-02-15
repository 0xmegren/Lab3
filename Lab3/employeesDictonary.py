employees = {}
while True:
    name = input("Enter employee name : ")
    if name == 'no':
        break
    salary = int(input("Enter employee salary :"))
    employees[name] = salary
print(employees)