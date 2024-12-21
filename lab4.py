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
# #in the terminal write python lab4 5 3
#2a

import math
# def is_prime(n):
#     if(n<2):
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if (n%i==0):
#             return False
#         else:
#             return True
# primeSum=0
# for num in range(2,1000):
#     if(is_prime(num)):
#         primeSum+=num
# print ("The sum of all prime numbers under 1000 is: ", primeSum)
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
# from collections import Counter
# string=input("Enter a string:")
# char_count=Counter(string)
# print("Character counts:")
# for char, count in char_count.items():
#     print(f"{char}:{count}")
#3a
import math
import re

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
# def unique_elements(lst):
#     return list(set(lst))
# lst=[1,2,3,4,4,5]
# print(f"Unique elements: {unique_elements(lst)}")

#4a
strings=["bat","bit","but","hat","hit","hut"]
pattern=r"b.t"
for s in strings:
    if re.match(pattern,s):
        print (s)
#4b
# import re
# text="john doe jane smith"
# matches=re.findall(r"\w+\s\w+", text)
# print ("Pairs of words:",matches)

#4c
import re
text="Smith, J Doe, A Brown, B"
matches=re.findall(r"(\w+),\s(\w)",text)
print("matches:", matches)


