#to count the frequency of each character in a string
a = input("Enter a string: ")
frequency = {}
for cha in a:
    if cha in frequency:
        frequency[cha] = frequency[cha] + 1
    else:
        frequency[cha] = 1

for cha, count in frequency.items():
    print(cha, ":", count)