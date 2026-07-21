dict1 = {
    "apple": 5,
    "banana": 3,
    "orange": 7,
    "grape": 2,
    "mango": 4
}

dict2 = {
    "banana": 6,
    "orange": 1,
    "mango": 8,
    "kiwi": 9,
    "pear": 5
}

merged_dic = dict1.copy()

for key,value in dict2.items():
    if key in merged_dic:
        merged_dic[key]+= value
    else:
        merged_dic[key] = value

print(merged_dic)