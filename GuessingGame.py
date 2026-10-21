import random
jackpot=random.randint(1,100)
guess=int(input("Guess The Number: "))
counter =1

while guess != jackpot:
    if guess < jackpot:
        print("Guess higher")
    else:
        print("Guess Lower")
    
    guess=int(input("Guess The Number: "))
    counter+=1

print("Sahi Jawab")
print("No of count:",counter)
    



