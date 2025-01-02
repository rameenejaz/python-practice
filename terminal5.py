def cumulative_product(list3):
    cumulativeList=[]
    product=1
    for item in list3:
        product*=item
        cumulativeList.append(product)
    return cumulativeList
input=[1,2,3,4]
result=cumulative_product(input)
print(f"The cumulative product of {input} is: {result}")