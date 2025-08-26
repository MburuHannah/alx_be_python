def perform_operation():
    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    operation=str(input("Enter the operation you want(add, subtract, multiply, divide:)".strip().lower()))
    match operation:
        case "add":
            print(num1+num2)
        case "subtract":
            print(num1-num2)
        case "multiply":
            print(num1*num2)

        case "divide":
            if num2==0:
                print("Error,Division by zero is not possible")
            else:
                print(num1/num2)
            
        case _:
            print("Invalid operation")  
            