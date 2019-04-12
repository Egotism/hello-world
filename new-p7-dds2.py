condition=0
x=0
while condition!=True:
    a=7*x
    condition = a%2==1 and a%3==2 and a%5==4 and a%6==5
    x+=1
if condition==True:
    print(a)

