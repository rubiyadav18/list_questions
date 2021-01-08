list=["a","1","2","5","b","q"]
n=int(input("enter a number"))
len_a=len(list)
i=1
while n>0:
    print(list[len_a-i])
    i=i+1
    n=n-1