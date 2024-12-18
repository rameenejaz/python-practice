def calculator ():
    print("Select Operation:")
    print ("1. Add")
    print ("2. Subtract")
    print ("3. Multiply")
    print ("4. Divide")
calculator()
choice=input("Enter choice 1/2/3/4:")
if choice in ('1','2','3','4'):
    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
        if (choice=='1'):
            print(f"The result is: {num1+num2}")
        elif(choice=='2'):
            print (f"The result is: {num1-num2}")
        elif(choice=='3'):
            print (f"The result is: {num1*num2}")
        elif(choice=='4'):
            if (num2!=0):
                print(f"The result is: {num1/num2}")
            else:
                print("Error! Division by zero is not allowed")
    except ValueError:
        print ("Error! Inavlid Input! Enter a numeric value:")
else:
    print("Invalid choice. Please select a valid operator")

#running the calculator

