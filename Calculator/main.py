def calculator():
    print("======================================")
    print("          Calculator          ")
    print("======================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("======================================")

    while True:
        ch = input("Enter your choice: ")

        if ch == "5":
            print("Exiting calculator. Goodbye!")
            break

        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if ch == "1":
            res = n1 + n2
            print(f"Result: {n1} + {n2} = {res}")
        elif ch == "2":
            res = n1 - n2
            print(f"Result: {n1} - {n2} = {res}")
        elif ch == "3":
            res = n1 * n2
            print(f"Result: {n1} * {n2} = {res}")
        elif ch == "4":
            if n2 != 0:
                res = n1 / n2
                print(f"Result: {n1} / {n2} = {res}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    calculator()