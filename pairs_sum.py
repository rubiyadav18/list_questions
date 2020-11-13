numbers=[10, 11, 12, 13, 14, 17, 18]
i=0
n=30
empty=[ ]
while i<len(numbers)-1:
    j=0
    while j<len(numbers):
        c=[ ]
        s=0
        s=s+numbers[i]+numbers[j]
        if numbers[i]+numbers[j]==n and numbers[i]<numbers[j]:
            c.append(numbers[i])
            c.append(numbers[j])
            empty.append(c)
        j=j+1
    i=i+1
print(empty)

