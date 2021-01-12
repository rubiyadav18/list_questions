list1=[7,8,9,-2,-1,-3,6,7,8]
i=0
z=len(list1)
while i<z:
    if list1[i]<0:
        list1.pop(i)
        # i am using pop because i want to remove -1 thats why i using pop fuction
        list1.insert(i,0)
    i=i+1
print(list1)
j=0
while j<len(list1):
    z=j
    while z<len(list1):
        if list1[z]>0:
            if list1[j]>list1[z]:
                t=list1[j]
                list1[j]=list1[z]
                list1[z]=t
        z=z+1
    j=j+1
print(list1)