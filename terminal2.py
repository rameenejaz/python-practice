number1=input("Enter number 1:")
number2=input("Enter number 2:")
number3=input("Enter number 3:")
largest=0
if number1 == number2 and number2 == number3:
    print("All numbers are equal")
elif (number1 == number2 and number1 > number3):
    largest = number1
    print(f"Number 1 and number 2 are equal and largest with value: {largest}")
elif (number2 == number3 and number2 > number1):
    largest = number2
    print(f"Number 2 is equal to number 3 and largest with value: {largest}")
elif (number1 == number3 and number1 > number2):
    largest = number1
    print(f"Number 1 is equal to number 3 and largest with value: {largest}")
elif (number1 > number2 and number1 > number3):
    largest = number1
    print(f"Number 1 is the largest with value: {largest}")
elif (number2 > number1 and number2 > number3):
    largest = number2
    print(f"Number 2 is the largest with value: {largest}")
else:
    largest = number3
    print(f"Number 3 is the largest with value: {largest}")