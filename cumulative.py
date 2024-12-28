factorial = 1
number = int(input("Enter an integer to find its factorial:"))
if number<0:
    print(f"factorial is not defined for negative numbers")
elif number==0:
    print(f"factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial*=i
print(f"The factorial of {number} is: {factorial}")