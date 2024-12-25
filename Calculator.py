def calculator():
    """
    A simple calculator with basic arithmetic operations.
    """

    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operation. Please enter +, -, *, or /.")
            continue

        print("Result:", result)

        choice = input("Do you want to perform another calculation? (y/n): ")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    calculator()
    