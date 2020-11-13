numbers=[1, 2, 3, 1, 2, 2, 3, 4,]
i=1
b=[ ]
index=0
while i<len(numbers):
    if numbers[index]==i:
        b.append(numbers)[i]
        index=index+i
    i=i+1
print(b)