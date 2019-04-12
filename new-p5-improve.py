temp=input("guess which number I am thinking now?\n"+"I guess it's:")
guess=int(temp)
answer=4
if guess==answer:
    print("Excellent！You are right!")
else:
    if guess > answer :
        print("No.It's too big!")
    if guess < answer:
        print("No.It's too small!")
print("--------End--------")
