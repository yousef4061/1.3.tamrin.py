a = float(input("enter first side: "))
b = float(input("enter second side: "))
c = float(input("enter third side: "))

if (a + b > c ) and (a * c > b) and (b + c > a):
    print("yes, a triangle can be formed")
else:
    print("no, a triangle cannot be formed")

#محسبه مثلث