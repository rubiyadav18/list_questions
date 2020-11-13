num=[1, 0, 0, 1, 1, 0, 1, 1,]
index=len(num)-1
decimal=0
c=1
while index>=0:
    decimal=decimal+num[index]*c
    c=c*2
    index=index-1
print(decimal)