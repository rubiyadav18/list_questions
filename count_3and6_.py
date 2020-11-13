list1=[2, 3, 4, 5, 3, 3, 3, 5,3, 3, 3, 3]
list2=[4, 5, 6, 6, 6, 6, 7, 7, 6, 6, 6,6]
i=0
empty1=[]
empty2=[]
# count=0
while i<len(list1):
    if list1[i]==3 and list2[i]==6:
        empty1.append(list1[i])
        empty2.append(list2[i])
        # count=count+1
    i=i+1
print(empty1)
print(empty2)