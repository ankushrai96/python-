a=int(input("enter side 1"))
b=int(input("enter side 2"))
c=int(input("enter side 3"))

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print("area of the traingle is :", area)