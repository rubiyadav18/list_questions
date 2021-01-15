n=int(input("entera number"))
e=[]
i=0
while i<n:
    p=int(input("enter a number"))
    e.append(p)
    i=i+1
print(e)
length=len(e)
j=0
count=0
while j<length-1:
    if e[j+1]-e[j]!=1:
        print("false")
        break
    if count==length-1:
        councount+1
    j=j+1
print("true")