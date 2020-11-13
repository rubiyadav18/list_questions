a=[50, 40, 23, 70, 56, 12,]
index=0
count=0
lenth=len(a)
while index<len(a):
    if a[index]>20 and a[index]<40:
        count=count+1
        print(a[index])
    index=index+1
print(count)