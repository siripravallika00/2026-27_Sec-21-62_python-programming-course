#Largest of three numbers (nested if)# Example solution: largest of three numbers using nested if
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print(f"Largest = {largest} (among {a}, {b}, {c})")