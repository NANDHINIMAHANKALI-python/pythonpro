def simple_calculator():
    try:
        # user input
        n1 = float(input("Enter n1 number : "))
        n2 = float(input("Enter n2 number : "))
        operators = input("Enter operators (+, -, *, /): ")

        # operation
        if operators == '+':
            result = n1 + n2
        elif operators == '-':
            result = n1 - n2
        elif operators == '*':
            result = n1 * n2
        elif operators == '/':
            result = n1 / n2
        else:
            print("Invalid operator")
            return

        # result
        print("Result:", result)

    except ValueError:
        print(" it is a Invalid input please enter a valid numbers.")

simple_calculator()
