#to print the grade of a student using an elif ladder 
marks = float(input("Enter marks: "))

if marks >= 90:
    print(f"Marks {marks}: Grade A")
elif marks >= 80:
    print(f"Marks {marks}: Grade B")
elif marks >= 70:
    print(f"Marks {marks}: Grade C")
else:
    print(f"Marks {marks}: Grade D")