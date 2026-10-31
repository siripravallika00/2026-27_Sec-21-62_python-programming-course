#to print numbers in a 3x3 grid
num = 1
row_loop_var = 1
while row_loop_var <= 3:
    for column_loop_var in range(1, 4):
        print(num, end=" ")
        num = num + 1
    print()
    row_loop_var = row_loop_var + 1