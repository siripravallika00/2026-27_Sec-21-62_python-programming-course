#sum of the two numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result=num1+num2
print(result)


#square of the number
num=int(input("Enter a number: "))
result=num*num
print(result)

# area and perimeter of a reactangle
num1=int(input("Enter the num1:"))
num2=int(input("Enter te num2:"))
area=num1*num2
perimeter=2*(num1+num2)
print("Area of rectangle",area)
print("perimeter of rectangle",perimeter)

# convert temperature from celsius to fahrenheit
celsius =int(input("Enter temperature in Celsius:"))
fahrenheit=(celsius*9/5)+32
print("Temperature in Fahrenheit:",fahrenheit)

# swap two numbers without using a third variable
a=5 
b=6
print("swapping of two numbers")
temp=a
a=b
b=temp
print("After swapping: a =",a,"b =",b)


#to calucuate a simple intrest
p=int(input("Enter principal amount:")) 
r=int(input("Enter rate of interest:")) 
t=int(input("Enter time in years:"))
si=(p*r*t)/100
print("Simple Interest is:",si)
