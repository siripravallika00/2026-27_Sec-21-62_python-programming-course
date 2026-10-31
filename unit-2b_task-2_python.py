#to print the multiplication table of a number
#1. using for loop
#2. using while

# multiplication table using a for loop
number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
# multiplication table using a while loop
number = int(input("Enter a number: "))
multiplier = 1
while multiplier <= 10:
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")
    multiplier = multiplier + 1