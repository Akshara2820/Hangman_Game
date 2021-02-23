import random
from images import IMAGES
from word import words1
print("hi")
name=input("enter your name--")
print("welcome to ",name,"to play HANGMAN Game \n")

print(" in this game you have to choice one latter in this game you have some chance if you give correct \n answer your chance will not cut but if you give wrong ans than your chance will cut \n")
print("guess any word--")
word=random.choice(words1)  
string=""

word1=[i for i in word]
gues=['_' for i in word]
chance=8
countofwronganswer=0
while chance>0:
    for i in gues:
        print(i,end=' ')

    print()
    a=input('enter any latter---')
    if a==word:
        print(" congratulations you win !!!!! ")
        break
    elif a in word1 and a in gues:
        print('you already guessed\n')
    elif a in word1:
        string=''
        l=0
        while l<len(word1):

            if word1[l]==a:
                string+=word1[l]
            elif gues[l]!='_':
                string+=gues[l]
            else:
                string+='_'
            l+=1
        gues=[i for i in string]
        if gues==word1:
            print(" congratulation /\ /\ you win\n ")
            chance=0
            break 
    else:
        print(IMAGES[countofwronganswer])
        chance=chance-1
        countofwronganswer+=1
        print('your guess is wrong')
        print("you have only this much chance",chance,"\n")
    
    if chance==0:
        print(' soo sad you lost ..',"your word is ",word)