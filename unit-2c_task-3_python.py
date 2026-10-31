#to print numbers in a 3x3 grid 
num = 1
for row_loop_var in range(1, 4):
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()