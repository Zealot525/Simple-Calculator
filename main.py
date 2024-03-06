from art import logo
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def division(n1,n2):
    return n1 / n2

operands = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : division,
}
def calculator():
    print(logo)
    end = False
    num1 = float(input("Enter the first number: "))
    while not end:
        for key in operands:
            print(key)
        operation = input("Enter the operation you want to perform: ")
        if operation != "+" and operation != "-" and operation != "*" and operation != "/":
            print("Invalid operation")
            end = True
        num2 = float(input("Enter the next number: "))
        answer = operands[operation](num1,num2)
        
        
        print(f"{num1} {operation} {num2} = {answer}")
        to_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:")
        if to_continue == "n":
            end = True
            calculator()
        if to_continue == "y":
            num1 = answer



calculator()