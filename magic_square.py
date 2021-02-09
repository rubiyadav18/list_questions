magic_square=[[8, 3, 4,],[1, 5, 9],[6, 7, 2],]
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
sum7=0
sum8=0
index=0
while index<len(magic_square):
    sum1=sum1+(magic_square[0][index])
    sum2=sum2+(magic_square[1][index])
    sum3=sum3+(magic_square[2][index])
    sum4=sum4+(magic_square[index][0])
    sum5=sum5+(magic_square[1][index])
    sum6=sum6+(magic_square[index][2])
    sum7=sum7+(magic_square[index][index])
    sum8=sum8+(magic_square[index][-index-1])
    print(sum1,sum2,sum3,sum4,sum5,sum6,sum7,sum8,)
    index=index+1
if sum1==sum2==sum3==sum4==sum5==sum6==sum7==sum8:
    print(magic_square)
else:
    print(not magic_square)

    