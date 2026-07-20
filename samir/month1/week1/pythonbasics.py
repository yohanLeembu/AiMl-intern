"""Basic Python Problems - Solved Examples

This file contains common beginner-level Python problem types with simple solutions.
Each example is written in a clean, easy-to-understand way.
"""

# 1. Basic Input / Output and Variables

def hello_world():
    print("Hello, World!")


def add_two_numbers(a, b):
    return a + b


def area_of_circle(radius):
    return 3.14 * radius * radius


# 2. Arithmetic and Operators

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"


def maximum_of_two(a, b):
    return max(a, b)


def maximum_of_three(a, b, c):
    return max(a, b, c)


# 3. Conditional Statements

def grade_result(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


# 4. Loops

def print_numbers_1_to_10():
    for i in range(1, 11):
        print(i, end=" ")
    print()


def print_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")


def sum_of_first_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 5. Strings

def reverse_string(text):
    return text[::-1]


def palindrome_check(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def count_words(sentence):
    return len(sentence.split())


# 6. Lists and Arrays

def list_sum(numbers):
    return sum(numbers)


def list_average(numbers):
    return sum(numbers) / len(numbers)


def find_largest(numbers):
    return max(numbers)


def find_smallest(numbers):
    return min(numbers)


def even_numbers_list(numbers):
    return [n for n in numbers if n % 2 == 0]


def remove_duplicates(items):
    return list(dict.fromkeys(items))


# 7. Tuples, Sets, and Dictionaries

def tuple_example():
    t = (1, 2, 3, 4)
    return t


def set_union(a, b):
    return set(a) | set(b)


def word_frequency(sentence):
    freq = {}
    for word in sentence.split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def dict_sorted_by_value(data):
    return dict(sorted(data.items(), key=lambda item: item[1], reverse=True))


# 8. Functions and Recursion

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)


def recursive_sum(n):
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)


# 9. Basic File Handling

def write_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


# 10. Exception Handling

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


def safe_int_conversion(value):
    try:
        return int(value)
    except ValueError:
        return "Invalid integer"


# 11. Basic OOP

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}")


# 12. Matrix / Nested List Example

def matrix_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total


# Demo section
if __name__ == "__main__":
    print("1. Hello World")
    hello_world()

    print("\n2. Add Two Numbers:", add_two_numbers(5, 7))
    print("Area of Circle:", area_of_circle(4))

    print("\n3. Even/Odd Check:", check_even_odd(10))
    print("Grade:", grade_result(85))
    print("Leap Year:", leap_year(2024))

    print("\n4. Loop Demo")
    print_numbers_1_to_10()
    print("Factorial of 5:", factorial(5))

    print("\n5. String Demo")
    print("Reverse:", reverse_string("python"))
    print("Palindrome:", palindrome_check("madam"))
    print("Vowels:", count_vowels("programming"))

    print("\n6. List Demo")
    numbers = [2, 4, 6, 8, 10]
    print("Sum:", list_sum(numbers))
    print("Average:", list_average(numbers))
    print("Even numbers:", even_numbers_list([1, 2, 3, 4, 5, 6]))

    print("\n7. Dictionary Demo")
    print(word_frequency("python python basics basics basics"))

    print("\n8. Recursive Demo")
    print("Recursive factorial of 5:", recursive_factorial(5))

    print("\n9. Exception Demo")
    print(divide(10, 0))
    print(safe_int_conversion("abc"))

    print("\n10. OOP Demo")
    student = Student("Samir", 101)
    student.display()
