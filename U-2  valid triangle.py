#valid triangle
a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))
if a<0 or b<0 or c<0:
    print("The triangle is not valid.")
else:
    if a + b > c and a + c > b and b + c > a:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")