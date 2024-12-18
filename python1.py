marks={}
print ("How many subjects do you want to add","\n")
z=int (input())
for y in range(z):
    print ("Enter name of subject", y+1, "\n")
    sub=str(input())
    print ("Enter obtained marks in the subject",sub,"\n")
    x=int(input())
    marks.update({sub:x})
    print (marks)