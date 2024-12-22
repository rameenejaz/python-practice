a=1
b=2
next=0
sum=0
while b<=1000:
    if b%2==0:
        sum+=b
        next = a + b
        a=b
        b=next
print(f"The sum of even valued items is: {sum}")