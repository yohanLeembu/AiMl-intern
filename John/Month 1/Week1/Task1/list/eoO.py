numbers = [84, 23, 150, 52, 7, 117, 68, 31, 139, 91, 14, 128, 45, 105, 79]

even = []
odd = []
for num in numbers:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)

print(even, odd)
