def display_result(a, b, result, operation):
    print("\n--- Result ---")
    print(f"Operation: {operation}")
    print(f"Decimal: {a} and {b} => {result}")
    print(f"Binary: {bin(a)} and {bin(b)} => {bin(result)}\n")

def main():
    while True:
        print("===== Bitwise Operations Menu =====")
        print("1. AND (&)")
        print("2. OR (|)")
        print("3. XOR (^)")
        print("4. NOT (~)")
        print("5. Left Shift (<<)")
        print("6. Right Shift (>>)")
        print("0. Exit")
        
        choice = input("Select an operation: ")

        if choice == "0":
            print("Exiting program... Goodbye!")
            break

        # Get numbers from user
        if choice in ["1", "2", "3"]:
            a = int(input("Enter first integer: "))
            b = int(input("Enter second integer: "))
            if choice == "1":
                result = a & b
                display_result(a, b, result, "AND")
            elif choice == "2":
                result = a | b
                display_result(a, b, result, "OR")
            elif choice == "3":
                result = a ^ b
                display_result(a, b, result, "XOR")

        elif choice == "4":
            a = int(input("Enter an integer: "))
            result = ~a
            print("\n--- Result ---")
            print(f"Operation: NOT")
            print(f"Decimal: {a} => {result}")
            print(f"Binary: {bin(a)} => {bin(result)}\n")

        elif choice in ["5", "6"]:
            a = int(input("Enter an integer: "))
            shift = int(input("Enter shift amount: "))
            if choice == "5":
                result = a << shift
                print("\n--- Result ---")
                print(f"Operation: Left Shift")
                print(f"Decimal: {a} << {shift} = {result}")
                print(f"Binary: {bin(a)} << {shift} = {bin(result)}\n")
            elif choice == "6":
                result = a >> shift
                print("\n--- Result ---")
                print(f"Operation: Right Shift")
                print(f"Decimal: {a} >> {shift} = {result}")
                print(f"Binary: {bin(a)} >> {shift} = {bin(result)}\n")

        else:
            print("Invalid choice. Please try again.\n")

if _name_ == "_main_":
    main()