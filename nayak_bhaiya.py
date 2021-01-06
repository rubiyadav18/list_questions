potion1=int(input("enter a any potion"))
potion2=int(input("enter a any potion"))
step1=int(input("enter a any step"))
step2=int(input("enter a any step"))
while potion1!=potion2:
    a=potion1+step1
    b=potion2+step2
    if a==b:
        print("meet",a)
        break
    else:
        print("no meet",a)
        break