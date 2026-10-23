try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
    answer = number1 / number2
    print(f"Answer: {answer}")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
    