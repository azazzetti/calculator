from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    should_accumulate = True
    while should_accumulate:

        for symbol in operations:
            print(symbol)
        operator = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))

        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            first_number = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()