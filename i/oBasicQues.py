import math
num1=int(input("Enter number 1:"))
num2=int(input("Enter number 1:"))
def sum(num1,num2):
    return num1+num2
def difference(num1,num2):
    if(num1>num2):
        return num1-num2
    else:
        return num2-num1
def product(num1,num2):
    return num1*num2
def quotient(num1,num2):
    if(num2!=0):
        return num1/num2
    elif (num2==0):
        print("Division with zero not possible")
print(f"The sum of num1 and num2 is:", sum(num1,num2))
print(f"The difference of num1 and num2 is:", difference(num1,num2))
print(f"The product of num1 and num2 is:", product(num1,num2))
print(f"The quotient of num1 and num2 is:", quotient(num1,num2))
