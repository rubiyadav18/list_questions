num=[10,80,50,40,30,20]
l=len(num)
i=0
while i<l:
    j=0
    while j<i:
        if num[i]>num[j]:
            pass
        j=j+1
         
    i+=1
    print(num[-j])