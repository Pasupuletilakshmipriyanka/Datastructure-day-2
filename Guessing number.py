import random
n=random.randrange(1,100)
guess=int(input("enter a number:"))
while n!=guess:
    if guess<n:
        print("Too low")
        guess=int(input("enter a number"))
    elif guess>n:
        print("Too high")
        guess=int(input("enter a number"))
    else:
        break
print("you guessed is right!")
                            
          
