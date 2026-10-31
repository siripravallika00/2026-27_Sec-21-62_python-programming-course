# Leap year — Approach 1 (nested if-else)
num = int(input("Enter a year: "))

if num % 400 == 0:
    print(f"{num} is a leap year")
else:
    if num % 100 == 0:
        print(f"{num} is not a leap year")
    else:
        if num % 4 == 0:
            print(f"{num} is a leap year")
        else:
            print(f"{num} is not a leap year")