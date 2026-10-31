#to count vowels, consonants, digits and spaces in a string
A = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for cha in A:
    if cha.lower() in "aeiou":
        vowels = vowels + 1
    elif cha.isalpha():
        consonants = consonants + 1
    elif cha.isdigit():
        digits = digits + 1
    elif cha == " ":
        spaces = spaces + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)