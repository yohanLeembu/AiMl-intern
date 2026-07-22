len = int(input("enter the lenght of the sequence: "))

first = 0
second = 1

for i in range(len):
    print(first, end=" ")
    third = first + second
    first = second
    second = third
