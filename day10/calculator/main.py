import art

print(art.logo)

def calculator():

    def add(n1, n2):
        """adding two numbers"""
        return n1 + n2

    def subtract(n1, n2):
        """subbtracting two numbers"""
        return n1 - n2

    def divide(n1, n2):
        """dividing two numbers"""
        return n1 / n2

    def multiply(n1, n2):
        """multyplying two numbers"""
        return n1 * n2
    
    
    operations = {
    "+": add, 
    "-": subtract, 
    "/": divide, 
    "*": multiply
    }

    num1 = float(input("What's the first number? "))

    for key in operations:
        print(key)

    operation_symbol = str(input("Pick an operation from the line above: "))

    num2 = float(input("What's the second number? "))

    for key in operations:
        if key == operation_symbol:
            answer = operations[key](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    should_continue = True

    while should_continue == True:
        another_number = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if another_number == "y":
            operation_symbol = str(input("Pick an operation: "))
            num4 = float(input("What's the next number? "))

            for key in operations:
                if key == operation_symbol:
                    num3 = answer
                    answer = operations[key](num3, num4)
                    print(f"{num3} {operation_symbol} {num4} = {answer}")

        else:
            should_continue = False
            calculator()

calculator()