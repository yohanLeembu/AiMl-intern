names = ["Alice", "Bob", "Charlie", "David", "Emma"]

with open('John/Month 1/Week1/Task1/inputOutput/name.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')
    
print('the names has been written')