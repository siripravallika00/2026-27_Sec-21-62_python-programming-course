# to check whether two strings are anagram check
p1 = input("Enter first string: ")
p2 = input("Enter second string: ")
if sorted(p1) == sorted(p2):
    print("Anagrams")
else:
    print("Not anagrams")