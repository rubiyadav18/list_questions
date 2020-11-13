element=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
sum1=0
sum2=0
while index<len(element):
    if element[index]%2==0:
        sum1=sum1+element[index]
        sum2=sum2+element[index]
    index=index+1
    sum2=sum2+4
print(sum1)
print(sum2)