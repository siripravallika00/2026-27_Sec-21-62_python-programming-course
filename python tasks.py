#sum of the two numbers(1)
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result=num1+num2
print(result)


#square of the number(2)
num=int(input("Enter a number: "))
result=num*num
print(result)

# area and perimeter of a reactangle(3)
num1=int(input("Enter the num1:"))
num2=int(input("Enter te num2:"))
area=num1*num2
perimeter=2*(num1+num2)
print("Area of rectangle",area)
print("perimeter of rectangle",perimeter)

# convert temperature from celsius to fahrenheit(4)
celsius =int(input("Enter temperature in Celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit:",fahrenheit)

# swap two numbers without using a third variable(5)
a=5 
b=6
print("swapping of two numbers")
temp=a
a=b
b=temp
print("After swapping: a =",a,"b =",b)


#to calucuate a simple intrest(6)
p=int(input("Enter principal amount:")) 
r=int(input("Enter rate of interest:")) 
t=int(input("Enter time in years:"))
si=(p*r*t)/100
print("Simple Interest is:",si)

#to caculate the compond intrest(7)
p=int(input("Enter principal amount:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time in years:"))
a=p*(1+r/100)**t
ci=a-p
print("Compound Interest is:",ci)

##first n natural numbers(8)
n = int(input("Enter the value of N: "))
sum = n * (n + 1) // 2
print("Sum of first", n, "natural numbers:", sum)

#arthemetic operation on two numbers(9)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

#relation operators(10) 
a = 10
b = 20
print("AND:", a < b and b > 15)
print("OR:", a > b or b > 15)
print("NOT:", not(a > b))

#logical operators(11)
a=2
result= a > 2 and  a<5 # logical and operator  
print("Result of ",a,"> 2 and",a,"<5 is",result)
#or(true)
a=6
result= a >2 or  a<5 # logical or operator
print("Result of ",a,"> 2 or",a,"<5 is",result)
#not(true)
a=7 
result= not(a >2 and  a<5) # logical not operator
print("Result of not(",a,"> 2 and",a,"<5) is",result)

#identity operatoes(12)
a=[1,2,3]
b=a 
result=b is a #is membership operator
print("result of ",b, "is not",a,"is :",result)
a=[1,2,3]
result=b is a # is membership operator
print("result of",b, "is not ",a,"is :",result)  

#membership operators(13)
a=[1,2,3]
b=a 
result=b is a #is membership operator
print("result of ",b, "is not",a,"is :",result)
a=[1,2,3]
result=b is a # is membership operator
print("result of",b, "is not ",a,"is :",result)


