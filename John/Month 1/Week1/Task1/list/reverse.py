numbers = [5, 12, 23, 34, 47, 56, 68, 79, 85, 99]
t_index = len(numbers)-1
reversed_num = []

for i in range(t_index, -1, -1):#the loop starts from 9 and then stops at 0
    reversed_num.append(numbers[i])#adding from the last element of the list to the first using indexes

print(reversed_num)
