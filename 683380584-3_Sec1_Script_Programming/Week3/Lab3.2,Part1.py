while True:
    try:
        start = int(input("Enter starting number for countdown: "))
        break
    except ValueError:
        print("Please Enter Number")

while start >= 0:
    print(start)
    start -= 1
print("Blast off!!")