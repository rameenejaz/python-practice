def dups(list1):
    countDups=0
    added=[]
    for i in list1:
        if list1.count(i)>1 and i not in added:
            countDups+=1
            added.append(i)
    return countDups
n=int(input("Enter the number of elements in the list:"))
list2=[]
for j in range(n):
    list2.append(int(input(f"Enter element {j+1}:")))
duplicates=dups(list2)
print(f"{duplicates} duplicate have been found in the list")