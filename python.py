'''The "Stone, Paper, Scissors" game, often abbreviated as "SPS,
" is a simple hand game usually played between two people. 
The game has three possible outcomes other than a tie: Stone
 beats Scissors, Scissors beats Paper, and Paper beats Stone.'''

import random

def assign(a):
    if(a==1):
        val="stone"
    elif(a==2):
        val="paper"
    elif(a==3):
        val="scissor"
    return val

def play(c,p):
    if(p=="stone"):
            if(c=='stone'):
                print("Match is tie")
            if(c=='paper'):
                print("You loss")
            if(c=='scissor'):
                print("You win")


    if(p=="scissor"):
            if(c=='stone'):
                print("You loss")
            if(c=='paper'):
                print("You win")
            if(c=='scissor'):
                print("Match is tie")
    
    if(p=="paper"):
            if(c=='stone'):
                print("You win")
            if(c=='paper'):
                print("Match is tie")
            if(c=='scissor'):
                print("You loss")



while(True):
    a=random.randint(1,3)
    comp=assign(a)
    

    b=int(input("\nstone-->1\npaper-->2\nscissor-->3\npress zero to stop playing \nenter value :-  "))
    if (b==0):
        break
    elif (b==1 or b==2 or b==3):
        person=assign(b)
        print("\n\n*********************************************************************************\n\n")
        print("your move is",person,"computer move is",comp)
        play(comp,person)
    else:
        print("\n\n*********************************************************************************\n\n")
        print("Enter valid option")