import turtle
import time
import random
from random import randint

words = ["hanger", "chairs", "pocket", "bodywash", "clothing",
         "computer", "python", "coding", "plastic", "jumper",
         "trunk", "bedtime", "friends", "time", "chemist",
         "decking", "suitcase", "knives", "armies", "shower"
         ]
hangmanword = 0
turtle.left(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(12.5)
turtle.right(90)

print("welcome to hangman!")
time.sleep(0.75)
print("generating random word...")
rand = random.randint(0, 19)
specificword = words[rand]
# print(specificword)
letterlist = list(specificword)
#print(letterlist)
lettercount = len(letterlist)
letterlistcomp = letterlist
# print(lettercount)
underscore = lettercount * '_'
undlist = list(underscore)
# print(undlist)
print("lets play!")

count = 0
head = 55
body = False
arms = False
leg1 = False
leg2 = False
hangmandone = False
while hangmandone == False:

    letter = input("Pick a letter...")
    if letter in letterlist:
        print("CORRECT")
        letterlocation = letterlistcomp.index(letter)
        # print(letterlocation)
        undlist[letterlocation] = [letter]
        print(undlist)
        letterlist = list(filter((letter).__ne__, letterlist))
        # print(letterlist)
        if '_' in undlist:
            hangmandone = False
        else:
            print("YOU WIN!!")
            hangmandone = True
            win = True
    else:
        print("WRONG")
        if head == 55:
            turtle.circle(25)
            turtle.circle(25, 180)
            head = True
        elif head == True:
            turtle.right(90)
            turtle.forward(75)
            body = True
            head = False
        elif body == True:
            turtle.left(180)
            turtle.forward(32.5)
            turtle.left(90)
            turtle.forward(25)
            turtle.right(180)
            turtle.forward(50)
            turtle.right(180)
            turtle.forward(25)
            turtle.left(90)
            turtle.forward(32.5)
            arms = True
            body = False
        elif arms == True:
            turtle.right(22.5)
            turtle.forward(45)
            turtle.left(180)
            turtle.forward(45)
            leg1 = True
            arms = False
        elif leg1 == True:
            turtle.right(157.5)
            turtle.left(22.5)
            turtle.forward(45)
            print("YOU LOOSE")
            hangmandone = True
            win = False

if win == False:
    print("The word was " + specificword)
