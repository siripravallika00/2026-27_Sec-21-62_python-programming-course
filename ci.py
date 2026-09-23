#to caculate the compond intrest(7)
p=int(input("Enter principal amount:"))
r=int(input("Enter rate of interest:"))
t=int(input("Enter time in years:"))
a=p*(1+r/100)**t
ci=a-p
print("Compound Interest is:",ci)