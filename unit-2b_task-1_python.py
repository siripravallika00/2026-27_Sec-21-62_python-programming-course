#Unit 2B Task 1: Print numbers from 1 to N — Approach 1 (for loop)
n = int(input("Enter the value of N: "))
for num in range(1, n + 1):
    print(f"{num}")

#Print numbers from 1 to N — Approach 2 (while loop)
n = int(input("Enter the value of N: "))
num = 1
while num <= n:
    print(f"{num}")
    num = num + 1