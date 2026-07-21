numbers = [47, 12, 89, 5, 34, 23, 78, 11, 56, 90]

len_num = len(numbers)

for i in range(len_num):
    for j in range(len_num-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1],numbers[j]

print(numbers)
