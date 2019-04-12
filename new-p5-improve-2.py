temp=input("guess which number I am thinking now?\n"+"I guess it's:")
guess=int(temp)
answer=4
while guess != answer:
    if guess > answer :
        print("No.It's too big!")
    else:
        print("No.It's too small!")
    temp = input ("Try again:")
    guess = int(temp)
if guess==answer:
    print("Excellent！You are right!")    
print("--------End--------")
