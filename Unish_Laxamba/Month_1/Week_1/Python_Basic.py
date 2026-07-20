# --- LISTS ---
# 1. Find the largest number
numbers = [4, 9, 2, 7]
print(max(numbers))

# 2. Add all numbers together
print(sum(numbers))

# 3. Reverse the order of a list
print(numbers[::-1])

# 4. Remove duplicate values
duplicates = [1, 2, 2, 3, 3, 3]
print(list(set(duplicates)))

# --- DICTIONARIES ---
# 5. Get a value from a dictionary safely
user = {"name": "Alice", "age": 25}
print(user.get("name"))

# 6. Combine two dictionaries together
dict1 = {"a": 1}
dict2 = {"b": 2}
print({**dict1, **dict2})

# 7. Print all the keys in a dictionary
print(user.keys())

# --- LOOPS & CONDITIONALS ---
# 8. Loop through a range and print numbers
for i in range(1, 6):
    print(i)

# 9. Simple if-else check
age = 20
print("Adult" if age >= 18 else "Minor")

# 10. Loop through items in a list
colors = ["red", "green", "blue"]
for color in colors:
    print(color)

# --- FUNCTIONS ---
# 11. Function that welcomes someone
def greet(name):
    return f"Hello, {name}!"
print(greet("Bob"))

# 12. Function that doubles a number
def double(x):
    return x * 2
print(double(5))

# 13. Function that checks if a word is "Python"
def is_python(word):
    return word == "Python"
print(is_python("Java"))

# --- FILE I/O ---
# 14. Create a file and write a single line of text
with open("test.txt", "w") as file:
    file.write("Hello from Python!")

# 15. Open a file and read its entire content
with open("test.txt", "r") as file:
    print(file.read())

# 16. Add a new line of text to the end of an existing file
with open("test.txt", "a") as file:
    file.write("\nAdding a new line.")

# --- MIXED / LOGIC ---
# 17. Count how many times a specific item appears in a list
items = ["apple", "banana", "apple", "cherry"]
print(items.count("apple"))

# 18. Convert a string to lowercase
text = "PYTHON PROGRAMMING"
print(text.lower())

# 19. Check if an item exists inside a list
fruits = ["apple", "banana", "orange"]
print("banana" in fruits)

# 20. Ask the user for their name and print a response
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")

# File I/O
# 21. Write a single line of text to a new file
with open("simple_note.txt", "w") as file:
    file.write("Learning Python is fun!")