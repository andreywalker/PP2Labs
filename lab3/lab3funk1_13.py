from random import random


import random
print("Hello! What is your name?")
name=input()
print("Well, "+name+", I am thinking of a number between 1 and 20.")
a=random.randrange(0,21)
print("Take a guess.")
i=0
b=int(input())
while b!=a:
    if b<a:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    i+=1
    b=int(input())
print("Good job, "+name+"! You guessed my number in "+str(i)+" guesses!")
