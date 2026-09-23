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
