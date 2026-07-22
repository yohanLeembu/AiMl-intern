def calculator():
    print("Calculator")
    print("Choose an operator: +, -, *, /")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print(f"Result: {result}")


if __name__ == "__main__":
    calculator()
