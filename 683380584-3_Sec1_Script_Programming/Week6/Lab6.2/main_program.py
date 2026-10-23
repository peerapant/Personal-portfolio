import math
import random
import my_utils  # Importing our custom module

def main():
    print("--- 1. Testing Custom Module (my_utils) ---")
    my_utils.greet("Alice")
    
    test_numbers = [7, 10, 13, 1]
    for num in test_numbers:
        result = my_utils.is_prime(num)
        print(f"Is {num} prime? -> {result}")
        
    print("\n--- 2. Testing Standard Library (math) ---")
    number = 25.0
    sqrt_value = math.sqrt(number)
    print(f"Square root of {number} using math.sqrt(): {sqrt_value}")
    
    print("\n--- 3. Testing Standard Library (random) ---")
    random_num = random.randint(1, 100)
    print(f"Random number between 1 and 100: {random_num}")

if __name__ == "__main__":
    main()