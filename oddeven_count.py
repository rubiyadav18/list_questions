elements=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index=0
count1=0
count2=0
while index<len(elements):
    if elements[index]%2==0:
        count1=count1+1
    else:
        count2=count2+1
    index=index+1
print(count1)
print(count2)