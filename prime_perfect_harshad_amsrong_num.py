num=int(input("enter a number"))
i=0
e=[ ]
while i<num:
    k=int(input("enter a number"))
    e.append(k)
    i=i+1
print(e)
prime=[]
prime.append("prime")
harshad=[ ]
harshad.append("harshad")
perfect=[ ]
perfect.append("perfect")
amstrong= [ ]
amstrong.append("amstrong")
strong=[]
strong.append("strong")
i=0
while i<len(e):
    
    b=1
    j=0
    while b<e[i]:
        if e[i]%b==0:
            j=j+1
        b=b+1
    if j==1:
        prime.append(e[i])
    
    r=e[i]
    sum=0
    while r>0:
        n=r%10
        sum=sum+n
        r=r//10
    if e[i]%sum==0:
        harshad.append(e[i])
    

    m=1
    sum=0
    while m < e[i]:
        if e[i]%m==0:
            sum=sum+m
        m=m+1
    if sum==e[i]:
        perfect.append(e[i])



    sum2=0
    q=e[i]
    while q>0:
        g=q%10
        sum2=sum2+g**3
        q=q//10
    if e[i]==sum2: 
        amstrong.append(e[i])




    user=e[i]
    sum3=0
    while user>0:
        x=1
        fact=0
        rem=e[i]%10
        while x<=rem:
            fact=fact*x
            x=x+1
        sum3=sum3+fact
        user=user//10
    if user==sum3:
        strong.append(e[i])

    i=i+1

print(prime)
print(harshad)
print(perfect)
print(strong)
print(amstrong)









