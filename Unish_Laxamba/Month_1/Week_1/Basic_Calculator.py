# BASIC CALCULATOR SCRIPT WITH ERROR HANDLING (LOOPING VERSION)


def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers.
    Includes a try-except block to safely catch division by zero."""
    try:
        return x / y
    except ZeroDivisionError:
        return "Error! Cannot divide by zero."


# --- 2. Define the Interactive Interface Function ---

def run_calculator():
    """Takes user inputs to select operations and perform calculations in a loop."""
    print("--- Welcome to the Python Function Calculator ---")
    
    while True:
        print("\nSelect an operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit Calculator")
        
        # Capture user choice
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user wants to exit right away
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break  # Breaks the while loop to terminate the function

        # Check if the user choice corresponds to a valid mathematical operation
        if choice in ['1', '2', '3', '4']:
            try:
                # Safely capture and convert user numeric inputs
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                # Handles cases where the user types letters instead of numbers
                print("Invalid input! Please enter numeric values only.")
                continue  # Skips the rest of the loop and starts over

            # Direct the logic based on the user's choice
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
                
        else:
            print("Invalid Selection! Please choose a number between 1 and 5.")

# --- 3. Execution Trigger ---
# This invokes the interaction block when you run the script
if __name__ == "__main__":
    run_calculator()