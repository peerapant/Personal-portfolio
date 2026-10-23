def greet(name: str) -> None:
    """Print a personalized greeting message."""
    print(f"Hello, {name}!")

def is_prime(number: int) -> bool:
    """
    Check if a number is prime.
    Returns True if prime, False otherwise.
    """
    if number <= 1:
        return False
    
    # Check divisors up to square root of number for efficiency
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True