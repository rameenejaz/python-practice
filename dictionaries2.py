address={'Wayne':'Young 678', 'John':'Oakwood 345', 'Mary':'Kingston 564'}
#iterating over a dictionary
for k in address.keys():
    print(k,":",address[k])
print("Sorting a dictionary:")
for k in sorted(address.keys()):
    print(k,":",address[k])
print("Printing keys and values")
for keys, value in address.items():
    print(f"{keys}:{value}")