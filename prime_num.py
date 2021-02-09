list=[2, 13, 17, 23, 22, 19, 32, 31]
empty=[]
index=0
while index<len(list):
    j=0
    b=2
    while b<(list[index]):
        if (list[index])%b==0:
            j=j+1
        b=b+1
    if j==0:
        empty.append(list[index])
    index=index+1
    print(empty)