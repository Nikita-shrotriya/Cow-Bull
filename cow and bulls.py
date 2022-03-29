from operator import index
import random
name=input("enter your name:")
print("*****************",name,"******************")
print("*****************Welcome to cowbull game*********************")
digit=5
def getsecertnum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getsecertnum()
    list=[]
    for i in range(digit):
        list.append(numbers[i])
    return list
def check_gusse():
    cow=[]
    bull=[]
    num=getclues()
    i=0
    print(num)
    maxguess=10
    while maxguess>0:
        guess=int(input("enter your guess="))
        position=int(input("enter your position"))
        if guess in num:
            index=num.index(guess)
            if index==position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("bull",bull)
                else:
                    print("You Already Used This digit Try  any Different digit")
            elif index!=position:
                cow.append(guess)
                print("cow",cow)
            else:
                print("Cow, This number is in list you can reuse it",cow)
        if num==bull:
            print(name,"congrestulation you win the game")
            break
        maxguess=maxguess-1
        print(maxguess,"your turns are left")
    else:
        print("You ran out your tries, You Loose The Game")   
    return bull
check_gusse()
def playagain():
    while True:
        again=input("if you want to play again press yes or no")
        if again=="yes":
            check_gusse()
        else:
            break
playagain()





