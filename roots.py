import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a==0):
    if(b==0):
        print("No root")

    else:
        x = -c/a
        print("root x=",x)
else:
    dalta = b*b-4*a*c
    if(dalta<0):
        print("No root")
    else:
        x1 = (-b-math.sqrt(dalta))/2*a
        x2 = (-b+math.sqrt(dalta))/2*a
        print("root x1=",x1)
        print("root x2=",x2)