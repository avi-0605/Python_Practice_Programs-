# Number Guessing (While Loop)SIMPLE  give 3 chance to guess 

import random 
a=random.randint(1,20)
print("================================== NUMBER GUSSSING GAME ================================")
print(" You have 2 chance to gusss the number ")
print("Hint : number lies between 1 to 20 ")
chance=0
while chance<3:
    guess=int(input("Enter your guess : "))
    if guess==a:
        print("YOU WON")
        break
    else:
        print("Wrong guess you have ",2-chance,"left.")
    chance+=1
if chance==3:
    print(" YOU LOST")
    print("The number was ",a) 
