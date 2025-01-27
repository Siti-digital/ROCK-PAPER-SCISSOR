import random as rnd
import os
def check(bot,stk):
    win=False
    if bot[0]=='R' and stk=='P' :
        win=True
    if bot[0]=='S' and stk=='R' :
        win=True
    if bot[0]=='P' and stk=='S' :
        win=True
    return(win)
    
    
    
def generate_stroke():
    strk=[]
    stroke=rnd.randint(1,3)
    if(stroke==1):
        strk=['R',"rock"]
    elif(stroke==2):
        strk=['P',"paper"]
    else:
        strk=['S',"scissors"]
    return(strk)
 
 
print("\n\n\t\t\t\t::::::::::::::INSTRUCTIONS::::::::::::::::::\n\n")
print("DIFFICULTY : INSANE ")
print("\n\nKEYSTROKES FOR THE GAME ")
print("\nROCK : 'R'    PAPER : 'P'   SCISSORS :  'S'  ")
print("\nTHE GAME HAS FOUR ROUNDS . EACH ROUNDS HAS 3 SUB-ROUNDS")
print("\nYOU HAVE TO DEFEAT THE BOT IN AT LEAST TWO SUB-ROUNDS TO WIN A ROUND")
print("\nROUND 3 AND 4 ARE THE SEMI-FINALS AND FINALS RESPECTIVELY")
print("\nYOU HAVE TO WIN ATLEAST TWO ROUNDS TO WIN THE ENTIRE GAME ")
print("\nBUT BE-AWARE THE BOT IS NOT THAT EASY TO DEFEAT")
print("\nHE IS NOT GOING TO LET YOU WIN SO EASILY")
print("\n\n\t\t\t\t::::::::: RULES ::::::::::::\n")
print("\nROCK WINS OVER SCISSORS")
print("\nPAPER WINS OVER ROCK")
print("\nSCISSORS WINS OVER PAPER")
print("\nIF BOTH KEY STROKES ARE SAME YOU LOSE \n\n\n")
print("\n\nPRESS ANY KEY TO START ................ ")
input()
os.system("cls")

sub_rounds=rounds=1
rounds_won=subrounds_won=0
while(rounds<=4):
    # print(rounds)
    if(rounds==3):
        print('\n\nSEMI-FINAL BEGINS \n\n')
    elif(rounds==4):
        print("\n\n FINAL ROUND BEGINS \n\n")
    subrounds_won=0
    sub_rounds=1
    while(sub_rounds<=3):
        # print(sub_rounds)
        if(rounds==3):
         print("\nROUND : SEMIFINAL SUB-ROUND : ",sub_rounds,"\n")
        elif(rounds==4):
         print("\nROUND : FINAL SUB-ROUND : ",sub_rounds,"\n") 
        else:
         print("\nROUND : ",rounds,"SUB-ROUND : ",sub_rounds,"\n")
        print("\nROUNDS WON : ",rounds_won,"SUB-ROUNDS WON : ",subrounds_won)
        if(rounds==3 and sub_rounds==1):
            print("\n\n\nBOT : C'MON BOY STRENGTHEN YOUR FIST \n")
        elif(rounds==1 and sub_rounds==1):
            print("\n\n\nBOT : GET READY TO LOSE BOY \n")
        elif(rounds==2 and sub_rounds==1):
            print("\n\n\nBOT : YOU HAVE GOT SOME BRAINS , BUT I AM GONNA BE HARSHER NOW \n")
        elif(rounds==4 and sub_rounds==1):
            print("\n\n\nBOT : IT'S TIME TO SHOW MY SKILLS TO YOU \n")
        choice=input("\nEnter your choice (R/P/S) : ")
        bot_stroke=generate_stroke()
        print("\nBOT : I had chosen ",bot_stroke[1])
        if(check(bot_stroke,choice)):
            print("\nYou won this sub-round")
            subrounds_won+=1
        else:
            print("\nYou lost this sub-round")
        print("\n\n-----------------------------------------------------------------------------\n\n")
        sub_rounds+=1
        if(subrounds_won>=2 and sub_rounds==4):
            print("\nYou won this round !!\n\n")
            rounds_won+=1
        elif(subrounds_won<3 and sub_rounds==4):
            print("\nYou lost this round !!\n\n")
    rounds+=1
    
if(rounds_won>=2):
    print("\n\nCONGRATS BOY YOU WON THE GAME , SEE YOU NEXT TIME\n\n ")
else:
    print("\n\nHAHA POOR BOY . I DEFEATED YOUN\n\n")
