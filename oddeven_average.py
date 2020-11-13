elements=[23, 14, 56, 12, 19, 15, 25, 31, 42, 43]
index=0
sum=0
while index<len(elements):
    if elements[index]%2==0:
        sum=sum+elements[index]
        print(sum//index)
    index=index+1
    