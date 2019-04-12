import random
chance=10
temp=input("guess which number I am thinking now?\n"+"I guess it's:")
test=temp.isdigit()
while test == False:
    temp=input("Just input a number please:")
    test=temp.isdigit()
guess=int(temp)
answer=random.randint(1,1000)
while guess != answer and chance >= 1:
    
    if guess > answer :
        print("No.It's too big!")
    else:
        print("No.It's too small!")

    chance-=1
    print(str(chance)+" chance ")

    
    if chance>=1:
        temp=input("Try again:")
        guess=int(temp)

if guess==answer:
    print("Excellent！You are right!")
else:
    print("No chance for you any more.You Lost.The answer is "+str(answer))
print("--------End--------")
