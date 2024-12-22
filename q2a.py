import math
sum=0
for i in range(2,1000):
    isPrime=True
    for j in range (2, int(math.sqrt(i)+1)):
        if (i%j==0):
            isPrime=False
            break
    if isPrime:
        sum+=i
print(f"The sum of all primes below 1000: {sum}")