import random 
length = int(input('Tell me how large should the numbers set me? :'))
num = int(input('Which number am i thinking?: '))

numbers = []

for i in range(1,length+1):
    numbers.append(i)

thinking_num = random.choice(numbers)
while(True):
    num = int(input('Wrong, Try Again: '))
    if num == thinking_num:
        print('Congrats, you won!!!')
        break