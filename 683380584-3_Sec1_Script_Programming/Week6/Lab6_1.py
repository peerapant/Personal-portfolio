def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers (a - b)."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float):
    """
    Return the quotient of two numbers.
    Handles division by zero by returning an error message.
    """
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Challenge: Power function with default parameter
def power(base: float, exponent: float = 2) -> float:
    """
    Return base raised to the power of exponent.
    Default exponent is 2 (squaring).
    """
    return base ** exponent


def main():
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Exit")
        
        choice = input("Select an operation (1-6): ").strip()
        
        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
            continue
            
        try:
            num1 = float(input("Enter first number: "))
            
            # Special case for power: optional exponent input
            if choice == '5':
                exp_input = input("Enter exponent (press Enter for default = 2): ").strip()
                if exp_input == "":
                    result = power(num1)
                else:
                    result = power(num1, float(exp_input))
            else:
                num2 = float(input("Enter second number: "))
                
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)
                    
            print(f"Result: {result}")
            
        except ValueError:
            print("Error: Invalid number input. Please enter valid numbers.")

if __name__ == "__main__":
    main()