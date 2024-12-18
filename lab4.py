#1a
def example():
    print ("This is not an indentation error")
example()
#1b
import math
def triangle():
    a=float(input("Enter the value of side 1:"))
    b=float(input("Enter the value of side 2:"))
    c=math.sqrt((a*a)+(b*b))
    print("The hypotenuse length is: ",c)
triangle()
#1c
import sys
if len(sys.argv)!=3:
    print("usage: python add.py num1 num2")
else:
    num1,num2=float(sys.argv[1]),float(sys.argv[2])
    print(f"Sum:{num1+num2}")
