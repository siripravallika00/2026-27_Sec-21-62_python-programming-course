#to count the number of digits in a number using while loop
number = int(input("Enter a number: "))

original_number = number
digit_count = 0

if number == 0:
    digit_count = 1
else:
    while number > 0:
        digit_count = digit_count + 1
        number = number // 10

print(f"Number of digits in {original_number} is {digit_count}")
