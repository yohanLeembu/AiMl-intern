with open('John/Month 1/Week1/Task1/inputOutput/name.txt', 'r') as file:
    lines = file.readlines()

number_of_lines = len(lines)

word_count = 0
char_count = 0

for line in lines:
    word_count += len(line.split())
    char_count += len(line)

print(word_count, char_count)
print(number_of_lines)

with open('John\Month 1\Week1\Task1\inputOutput\student.csv','r') as file:
    lines = file.readlines()

values = lines
key = values.pop(0).strip().split(',')

f = []

for line in values:
    value = line.strip().split(',')
    student={}
    for i in range(len(key)):
        student[key[i]] = value[i]
    f.append(student)

for line in f:
    print(line)