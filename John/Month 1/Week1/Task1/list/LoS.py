numbers = [84, 23, 150, 52, 7, 117, 68, 31, 139, 91, 14, 128, 45, 105, 79]


#using functions
print(f'{min(numbers)} is the smallest and {max(numbers)} is the largest')

#using logic
largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    
    if num < smallest:
        smallest = num

print(f'The smallest is {smallest}, and the largest is {largest}')


