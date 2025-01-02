#1a
# def example():
#     print ("This is not an indentation error")
# example()

#1b
# import math
# def triangle():
#     a=float(input("Enter the value of side 1:"))
#     b=float(input("Enter the value of side 2:"))
#     c=math.sqrt((a*a)+(b*b))
#     print("The hypotenuse length is: ",c)
# triangle()

#1c
# import sys
# if len(sys.argv)!=3:
#     print("usage: python add.py num1 num2")
# else:
#     num1,num2=float(sys.argv[1]),float(sys.argv[2])
#     print(f"Sum:{num1+num2}")

#2a
# import math
# sum=0
# for i in range(2,1000):
#     isPrime=True
#     for j in range (2, int(math.sqrt(i)+1)):
#         if (i%j==0):
#             isPrime=False
#             break
#     if isPrime:
#         sum+=i
# print(f"The sum of all primes below 1000: {sum}")

#2b (sum of the even fibonacci sequence
# def fibonacci(limit):
#     a,b=1,2
#     evenSum=0
#     while(a<=limit):
#         if (a%2==0):
#             evenSum+=a
#         a=b
#         b=a+b
#     return evenSum
# print(f"The sum of the even fibonacci numbers below 4 million is: {fibonacci(4000000)}")

#2c
# sentence=str(input("Enter a word or sentence to count char:"))
# char_count_dict={}
# for char in sentence.lower():
#     if char in char_count_dict:
#         char_count_dict[char]+=1
#     else:
#         char_count_dict[char]=1
# print(f"Character counts: {char_count_dict} ")
#3a
# import math
# def ball_collide(ball1, ball2):
#     x1, y1, r1=ball1
#     x2, y2, r2=ball2
#     distance=math.sqrt((x2-x1)**2 + (y2-y1)**2)
#     return distance<=(r1+r2)
#
# ball1 =(0,7,2)
# ball2 =(3,0,2)
# print(f"Do the balls collide? {ball_collide(ball1,ball2)}")

#3b
# def unique_elements(list):
#     return list(set(list))
# lst=[1,2,3,4,4,5]
# print(f"Unique elements: {unique_elements(lst)}")

#4a
# import re
# strings = ["bat", "bit", "but", "hat", "hit", "hut", "cat", "bot"]
# # Regular expression to match the desired strings
# pattern = r'\b[bh][aiu]t\b'
# # Filter strings that match the pattern
# matched_strings = [s for s in strings if re.match(pattern, s)]
# print("Matched strings:", matched_strings)

#4b
# import re
# text="john doe jane smith"
# matches=re.findall(r"\w+\s\w+", text)
# print ("Pairs of words:",matches)
#4c
# import re
# text="Smith, J Doe, A Brown, B"
# matches=re.findall(r"(\w+),\s(\w)",text)
# print("matches:", matches)

#5
# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number:"))
# temp=0
# temp=num1
# num1=num2
# num2=temp
# print(f"Num1={num1}")
# print(f"Num2={num2}")

#6
# def sum(a,b):
#     return a+b
# def difference(a,b):
#     if(a>=b):
#         return a-b
#     if(a<b):
#         return b-a
# def product(a,b):
#     return a*b
# def quotient(a,b):
#     if (b==0):
#         print("division with zero not possible")
#     return float(a/b)
# a=int(input("Enter the value of a: "))
# b=int(input("Enter the value of b:"))
# input=int(input("Enter choice 1-4 (1 for addition, 2 for subtraction, 3 for multiplication or 4 for division: "))
# if input==1:
#     addition=sum(a,b)
#     print(f"The sum of {a} and {b} is: {addition} ")
# if input==2:
#     minus=difference(a,b)
#     print(f"The difference between {a} and {b} is {minus}")
# if input==3:
#     product=product(a,b)
#     print(f"The product of {a} and {b} is {product}")
# if input==4:
#     division=quotient(a,b)
#     print(f"The quotient is {a} and {b} is {division}")
