numbers=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
b=[ ]
while i<len(numbers):
    j=i+1
    count=0
    while j<len(numbers):
        if numbers[i]==numbers[j]:
            count=count+1
        j=j+1
    if numbers[i] not in b and count>0:
        b.append(numbers[i])
    i=i+1
print(b)
