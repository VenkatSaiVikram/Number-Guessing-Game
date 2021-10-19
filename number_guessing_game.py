import random
print("---------------------------------------------------------- \n \n         HI, WELCOME TO THE GAME OF GUESSING...")
user_score=0
score=0
enter=""
while enter=="":
    Range=input("----------------GUIDE TO SELECT YOUR RANGE---------------- \nA for range(0-10)  \nB for range(0-25)  \nC for range(0,50) \nD for range(0,100)  \nE for (to enter custom range)  \n-------------------------------------- \nENTER THE RANGE : ")
    print("--------------------------------------")
    while Range.upper()=="A" :
        computer_guess=random.randint(0,10)
        difficulty_level=input("----------DIFFICULTY LEVEL------------  \nA for LOW-(5 guesses)  \nB for MEDIUM-(3 guesses)  \nC for EXPERT-(1 guess) \n--------------------------------------  \nENTER DIFFICULTY LEVEL : ")
        print("--------------------------------------")
        print()
        if difficulty_level.upper()=="A":
            print("-----------------------GUESS(0-10)-------------------------")
            for i in range(5):
                user_guess=int(input("ENTER GUESS : "))
                ascore=0
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    ascore+=0
                    user_score+=score                
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    ascore+=1
                    user_score+=ascore
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    ascore+=0
                    user_score+=score
            if ascore==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
            print()
            print("----------------------------------------------------------")
        elif difficulty_level.upper()=="B":
            print("-----------------------GUESS(0-10)-------------------------")
            for i in range(3):
                user_guess=int(input("ENTER YOUR GUESS : "))
                bscore=0
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    bscore+=0
                    user_score+=score
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    bscore+=1
                    user_score+=bscore
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    bscore+=0
                    user_score+=score
            if bscore==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break
            print("----------------------------------------------------------")
        elif difficulty_level.upper()=="C" :
            print("-----------------------GUESS(0-10)-------------------------")
            for i in range(1):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=score
                    break
                elif user_guess!=computer_guess:
                    print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    break
        break
    while Range.upper()=="B" :
        computer_guess=random.randint(0,25)
        difficulty_level=input("----------------ENTER-----------------  \nA for LOW-(7 guesses)  \nB for MEDIUM-(5 guesses)  \nC for EXPERT-(3 guesses) \n--------------------------------------  \nENTER DIFFICULTY LEVEL : ")
        print("--------------------------------------")
        print()
        if difficulty_level.upper()=="A":
            print("-----------------------GUESS(0-25)-------------------------")
            for i in range(7):
                user_guess=int(input("ENTER GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
        elif difficulty_level.upper()=="B":
            print("-----------------------GUESS(0-25)-------------------------")
            for i in range(5):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break
        elif difficulty_level.upper()=="C" :
            print("-----------------------GUESS(0-25)-------------------------")
            for i in range(3):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break                
        break
    while Range.upper()=="C" :
        computer_guess=random.randint(0,50)
        difficulty_level=input("----------------ENTER-----------------  \nA for LOW-(15 guesses)  \nB for MEDIUM-(10 guesses)  \nC for EXPERT-(7 guesses) \n--------------------------------------  \nENTER DIFFICULTY LEVEL : ")
        print("--------------------------------------")
        print()
        if difficulty_level.upper()=="A":
            print("-----------------------GUESS(0-50)-------------------------")
            for i in range(15):
                user_guess=int(input("ENTER GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
        elif difficulty_level.upper()=="B":
            print("-----------------------GUESS(0-50)-------------------------")
            for i in range(10):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break
        elif difficulty_level.upper()=="C" :
            print("-----------------------GUESS(0-50)-------------------------")
            for i in range(7):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break                
        break
    while Range.upper()=="D" :
        computer_guess=random.randint(0,100)
        difficulty_level=input("----------------ENTER-----------------  \nA for LOW-(25 guesses)  \nB for MEDIUM-(15 guesses)  \nC for EXPERT-(10 guesses) \n--------------------------------------  \nENTER DIFFICULTY LEVEL : ")
        print("--------------------------------------")
        print()
        if difficulty_level.upper()=="A":
            print("-----------------------GUESS(0-100)-------------------------")
            for i in range(25):
                user_guess=int(input("ENTER GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
        elif difficulty_level.upper()=="B":
            print("-----------------------GUESS(0-100)-------------------------")
            for i in range(15):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break
        elif difficulty_level.upper()=="C" :
            print("-----------------------GUESS(0-100)-------------------------")
            for i in range(10):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE\nCOMPUTER's NUMBER :", computer_guess)
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...")
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break                
        break
    while Range.upper()=="E" :
        lower_limit=int(input("ENTER LOWER LIMIT OF YOUR RANGE : "))
        upper_limit=int(input("ENTER UPPER LIMIT OF YOUR RANGE : "))
        computer_guess=random.randint(lower_limit,upper_limit)
        a=(upper_limit-lower_limit)//3
        b=(upper_limit-lower_limit)//4
        c=(upper_limit-lower_limit)//5
        print("----------------ENTER-----------------  \nA for LOW (",a,"guesses) \nB for MEDIUM (",b,"guesses)  \nC for EXPERT (",c,"guesses) \n-------------------------------------- ")
        difficulty_level=input("ENTER DIFFICULTY LEVEL : ")
        print("--------------------------------------")
        print()
        if difficulty_level.upper()=="A":
            print("-------------------GUESS(", lower_limit ,",", upper_limit ,")---------------------")
            for i in range(15):
                user_guess=int(input("ENTER GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
        elif difficulty_level.upper()=="B":
            print("-------------------GUESS(", lower_limit ,",", upper_limit ,")---------------------")
            for i in range(10):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\nCOMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break
        elif difficulty_level.upper()=="C" :
            print("-------------------GUESS(", lower_limit ,"-", upper_limit ,")---------------------")
            for i in range(7):
                user_guess=int(input("ENTER YOUR GUESS : "))
                if user_guess<computer_guess:
                    print("YOUR GUESS IS LESSER THAN COMPUTER's ONE")
                    user_score+=0
                elif user_guess==computer_guess:
                    print("YOU WON THE GAME,YOUR GUESS IS CORRECT...\nCOMPUTER's NUMBER :", computer_guess)
                    print("----------------------------------------------------------")
                    user_score+=1
                    break
                elif user_guess>computer_guess:
                    print("YOUR GUESS IS GREATER THAN COMPUTER's ONE")
                    user_score+=0
            if user_score==0:
                print("YOU LOST THE GAME,YOU DIDN'T GUESS THE CORRECT NUMBER...\n COMPUTER's NUMBER :", computer_guess)
                print("----------------------------------------------------------")
                break 
        break
    print("YOUR SCORE IS",user_score)               
    enter=input("PRESS ENTER TO PLAY AGAIN OR PRESS ANY KEY TO EXIT : ")
