numbers = [12, 45, 7, 23, 45, 89, 12, 34, 56, 7, 78, 90, 23, 11, 56]

unique_num = []

for num in numbers:
    if not num in unique_num:
        unique_num.append(num)

print(unique_num)
