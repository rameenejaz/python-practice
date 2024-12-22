import math
x1=float(input("Enter the value of coordinates of x1:"))
y1=float(input("Enter the value of coordinates of y1:"))
x2=float(input("Enter the value of coordinates of x2:"))
y2=float(input("Enter the value of coordinates of y2:"))
distance= math.sqrt((x2-x1)**2 +(y2-y1)**2)
print(f"The distance between the two points is: {distance:.2f}")
