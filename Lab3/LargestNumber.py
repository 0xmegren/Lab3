List = []
for i in range(10):
    num = int(input("input value: "))
    List.append(num)
largest = List[0]
for number in List:
    if number > largest:
        largest = number
print("The largest number is: " + str(largest) )