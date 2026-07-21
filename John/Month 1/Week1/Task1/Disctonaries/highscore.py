students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Emma": 88,
    "Frank": 81,
    "Grace": 90
}

highest_student = list(students.keys())[0]
highest_score = students[highest_student]

for key,score in students.items():
    if score > highest_score:
        highest_score = score
        highest_student = key

new = list(students.items())
len_stud = len(new)

for i in range(len_stud):
    for j in range(len_stud-1):
        if new[j][1] < new[j+1][1]:
            new[j], new[j+1] = new[j+1], new[j]
for i,stud in enumerate(new, 1):
        print(f'{i}. {stud[0]} : {stud[1]} marks.')

print(f'The highest scoring student is {highest_student}.')