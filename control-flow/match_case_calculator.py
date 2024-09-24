num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

operator = input("Choose the operation (+, -, *, /): *")

match operator:
    case "+":
        result = num2 + num1
        print(f"The result is {result}")
    case "-":
        result = num2 - num1
        print(f"The result is {result}")
    case "*":
        result = num2 * num1
        print(f"The result is {result}")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else: 
            result = num2 / num1
            print(f"The result is {result}")

    