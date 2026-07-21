dict = {
    "apple": 5,
    "banana": 3,
    "orange": 7,
    "grape": 2,
    "mango": 4
}
inverted_values = {}
for key,value in dict.items():
    inverted_values[value] = key

print(inverted_values)