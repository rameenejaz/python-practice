#Name: Rameen Muzammil Ejaz
#Registration number: FA24-BSE-160
#Section: A
#Task 1:
# number=input("Enter a 4 digit number:")
# reverse= ""
# for value in number:
#     reverse= value +reverse
# print(f" {number} when reversed is: {reverse} ")

#Task 2:
# number1=input("Enter number 1:")
# number2=input("Enter number 2:")
# number3=input("Enter number 3:")
# largest=0
# if number1 == number2 and number2 == number3:
#     print("All numbers are equal")
# elif (number1 == number2 and number1 > number3):
#     largest = number1
#     print(f"Number 1 and number 2 are equal and largest with value: {largest}")
# elif (number2 == number3 and number2 > number1):
#     largest = number2
#     print(f"Number 2 is equal to number 3 and largest with value: {largest}")
# elif (number1 == number3 and number1 > number2):
#     largest = number1
#     print(f"Number 1 is equal to number 3 and largest with value: {largest}")
# elif (number1 > number2 and number1 > number3):
#     largest = number1
#     print(f"Number 1 is the largest with value: {largest}")
# elif (number2 > number1 and number2 > number3):
#     largest = number2
#     print(f"Number 2 is the largest with value: {largest}")
# else:
#     largest = number3
#     print(f"Number 3 is the largest with value: {largest}")

#Task 3:
# tuple=(5,25,35,106,81,224,675)
# number=int(input("Enter a number to search in the tuple:"))
# index=-999
# for i in range(len(tuple)):
#     if tuple[i]==number:
#         index=i
#         break
# if index!=-999:
#     print(f"Number {number} is found at index {index}")
# else:
#     print(f"{number} not found in tuple")

#Task 4:
# def dups(list1):
#     countDups=0
#     added=[]
#     for i in list1:
#         if list1.count(i)>1 and i not in added:
#             countDups+=1
#             added.append(i)
#     return countDups
# n=int(input("Enter the number of elements in the list:"))
# list2=[]
# for j in range(n):
#     list2.append(int(input(f"Enter element {j+1}:")))
# duplicates=dups(list2)
# print(f"{duplicates} duplicate have been found in the list")

#Task 5
# def cumulative_product(list3):
#     cumulativeList=[]
#     product=1
#     for item in list3:
#         product*=item
#         cumulativeList.append(product)
#     return cumulativeList
# input=[1,2,3,4]
# result=cumulative_product(input)
# print(f"The cumulative product of {input} is: {result}")