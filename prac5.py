# nums=[1,4,5,9,8,7,81,100,102,110,115]
# idx=0
# while idx<len(nums):
#     print(nums[idx])
#     idx+=1
#search a number in a tuple
# nums=(1,4,5,9,8,7,81,100,102,110,115,81)
# x=81
# index=0
# while index<len(nums):
#     if(nums[index]==x):
#         print("Found at index", index)
#         break
#     index+=1
#     print("End of loop search")

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1
# print("End of loop")

# nums=(1,4,5,9,8,7,81,100,102,110,115,81)
# for val in nums:
#     print(val)
# str="ComsatsUni"
# for char in str:
#     print (char)
# for el in range(5):
#     print(el)
# for el in range(1,5):
#     print (el)
# for el in range (1,10,2):
#     print(el)
# for even in range (2,10,2):
#     print (even)
# for odd in range(1,12,2):
#     print(odd)
# n=int(input("Enter a number: "))
# sum=0
# counter=1
# while counter<=n:
#     sum+=counter
#     counter+=1
# print(sum)

number=int(input("Enter a number:"))
factorial=1
counter=1
while counter<=number:
    factorial=counter*factorial
    counter+=1
print(f"The factorial of {number} is ",factorial)
