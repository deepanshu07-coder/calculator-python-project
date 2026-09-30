def calculate(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operator: {op}")


def main():
    print("Simple Calculator")
    print("Operators: +  -  *  /")
    print("Type 'q' to quit\n")

    while True:
        expr = input("Enter expression (e.g. 5 + 3): ").strip()
        if expr.lower() == 'q':
            print("Goodbye!")
            break

        parts = expr.split()
        if len(parts) != 3:
            print("Please enter in the form: number operator number\n")
            continue

        num1_str, op, num2_str = parts
        try:
            num1 = float(num1_str)
            num2 = float(num2_str)
            result = calculate(num1, op, num2)
            print(f"Result: {result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        except ZeroDivisionError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
