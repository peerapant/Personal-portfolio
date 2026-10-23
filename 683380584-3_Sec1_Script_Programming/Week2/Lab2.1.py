num = int(input("Enter a number: ") )
if num < 0:
    text = f"{num} is negative"
elif num > 0:
    text = f"{num} is positive"
else:
    text = f"{num} is zero"

if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"

print(f"{text} and {result}")