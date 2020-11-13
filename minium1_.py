numbers=[5, 40, 23, 1, 7, 5, 2, 4,3,]
index=numbers
i=0
while i<len(numbers):
    if numbers[i]<index:
        index=numbers[i]
    i=i+1
print(index)
