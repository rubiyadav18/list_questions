a=['hello muskan how are you','i am fine','how are you','i am rubi yadav']
i=0
c=0
while i<len(a):
    j=0
    while j<len(a[i]):
            c=c+len(a[i][j])
            j+=1
    i+=1
print(c)