#to check whether a string is a palindrome
P = input("Enter a string: ")
if P == P[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")