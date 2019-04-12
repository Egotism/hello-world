chance=3
print("chance = " + str(chance))
secret=4
temp=input("Guess what I am thinking?/n"+"I think it is :")
guess=int(temp)

while chance >=1:
    
    if guess==secret:
        print("Excellent！You are right!")
        break
    else:
        if guess > secret :
            print("No.It's too big!")
        else:
            print("No.It's too small!")

        chance-=1
        print("chance = " + str(chance))
        if chance == 0:
            print("No chance.Sorry.")
            break
        else:
            temp = input ("Try again:")
            guess = int(temp)
            
    
    

print("--------End--------")


        
