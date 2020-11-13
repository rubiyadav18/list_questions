a=[50, 40, 23, 70, 56, 12,]
i=0
min=0
while i<len(a):
    if a[i]<min:
        min=a[i]
    i=i+1
    print(min)