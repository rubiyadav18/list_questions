numbers=[ 8950, -40, -23, -2, -5, -120,]
i=0
index=0
second=numbers[0]
m=numbers[0]
while index<len(numbers):
    if numbers[index]>m:
        m=numbers[index]
    else:
        second=numbers[index]
    index=index+1
while i<len(numbers):
    if second<numbers[i]<m:
        second=numbers[i]
    i=i+1
print(m,second)