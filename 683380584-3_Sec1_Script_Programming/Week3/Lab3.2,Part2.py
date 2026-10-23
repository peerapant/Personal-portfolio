import random

secret_number = random.randint(1,100)
limit = 10
while limit != 0:
    while True:
        try:
            guess = int(input("Guess the number: "))
            break
        except ValueError:
            print("Please Enter Number")

   
    if guess < secret_number:  #เติมเงื่อนไขให้สมบูรณ์
        print(f"{guess} is too low! Try again.")
        limit -= 1
        print(f"Remaining attempts : {limit}")
    elif guess > secret_number:  #เติมเงื่อนไขให้สมบูรณ์
        print(f"{guess} is too high! Try again.")
        limit -= 1
        print(f"Remaining attempts : {limit}")
    else:
        print("Congratulations! You guessed it!")
        break
print("\nNo attempts remaining")