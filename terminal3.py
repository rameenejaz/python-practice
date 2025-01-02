tuple=(5,25,35,106,81,224,675)
number=int(input("Enter a number to search in the tuple:"))
index=-999
for i in range(len(tuple)):
    if tuple[i]==number:
        index=i
        break
if index!=-999:
    print(f"Number {number} is found at index {index}")
else:
    print(f"{number} not found in tuple")
