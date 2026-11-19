import random

##print signature
def print_signature():
    print("NAME: Manasa Rajesh Kumar\nSTUDENT #: 400680382\nENG 1P13: Integrated Cornerstone Design Projects in Engineering\nPROFESSOR NAME: Sam Scott \nTERM: FALL 2026")

##first scene
def enter (choice,code):
    suspicion1=0

    firstdigit=code//100                                                                                        #getting the first digit of the code
    for i in range (3):
        guard=random.randint(1,6)

        if choice<guard:
            suspicion1+=1
    if choice>0 and choice<=6:
        print(f"\nThe guard noticed you {suspicion1} number of times")
    if choice >=4 and choice<=6:                                                                                #values to return depending on the choice made by user
        if code<500:
            clue=-1
            return(suspicion1, clue)
        else:
            clue=-2
            return(suspicion1, clue)
    elif choice<4 and choice>0:
        return(suspicion1, firstdigit)

##second scene
def side_room(investigate, code):
    if investigate==True:
        print("\nYou step into a maintenance room packed with tools and equipment, looking for a clue....")       #Happens if the user wants to investigate a side room
        num=random.randint(1,100)
        if num>80:
            clue=code
        elif num>30 and num<=80:
            clue=(code%10)
        else:
            clue= -1
        if num%20==0:                                                                                           #logic for rounding up the suspicion
            suspicion2=(num//20)
        else:
            suspicion2=(num//20)+1
    elif investigate==False:
        print("You skipped a room")                                                                             #Happens if the user doesnt want to investigate a side room
        clue=-1
        suspicion2=0
    return(suspicion2, clue)

##third scene
def crack_code(suspicion,code):
    suspicion3=0
    print(f"\nYou have time for {10-suspicion} number of guesses!! ")
    for i in range(10-suspicion):                                                                              #Asking user to guess the code n number of times
        guess=int(input("enter your guess (3-digit code): "))
        if guess!=code:
            print(f"\nAttempt:{i+1} Guess:{guess}, incorrect")
            suspicion3+=1
        else:
            print(f"\nAttempt:{i+1} Guess:{guess}, correct")

            break
    if guess!=code:
        suspicion3+=3
    if guess==code:
        return(suspicion3, True)
    else:
        return(suspicion3, False)

##escape final scene
def escape(suspicion):
    danger=suspicion//3                                                                                     #logic for assigning danger
    progress=0
    while progress<10 and danger<10:
        action=input("\n have been spotted again do you want to run(1),hide(2), or find a shortcut(3)[type 1,2 or 3]:")
        if action =="1":
            num=random.randint(1,100)
            if num<=60:
                progress+=1
                print(f"\nYou are running away, Progress = {progress}, danger = {danger}")
            else:
                progress+=1
                danger+=1
                print(f"\nYou are running away but youve been noticed!, Progress = {progress}, danger = {danger}")
        elif action =="2":
            num=random.randint(1,100)
            if num<=80:
                progress+=1
                print(f"\n succesfully hid away from the guard, Progress = {progress}, danger = {danger}")
            else:
                danger+=2
                print(f"\nYou have been spotted, Progress = {progress}, danger = {danger}")
        elif action=="3":
            num=random.randint(1,100)
            if num<=50:
                progress+=3
                print(f"\nYou found a shortcut, Progress = {progress}, danger = {danger}")
            else:
                danger+=3
                print(f"\nYou reached a dead end, Progress = {progress}, danger = {danger}")
        else:
            print("\nPLEASE CHOOSE 1, 2 or 3 ")                                                                 #In case the user does'nt choose a valid input

    return(progress)

##heist
def heist(name):
    print(f"\nHello {name}, Your mission is to infiltrate the building, find clues to the secret code, crack the safe, and escape before security catches you!")
    while True:
        code=random.randint(100,999)
        if DEBUG==True:                                                                                         #Used for debugging to get the code early
            print(f"code={code}")
#scene1
        choice=int(input("\nChoose a number from 1-6 to decide how you enter the room.\n1.Break through the main door.\n2.Climb through a window.\n3.Sneak through a vent.\n4.Use a stolen keycard.\n5.Disguise yourself as a worker.\n6.Enter through the staff entrance.\n\nCAUTION: lower the number higher the risk of getting caught: "))
        while True:
            if choice>=1 and choice<=6:                                                                          #If user gives a valid input a clue will be given
                suspicion1, clue = enter(choice,code)
                if clue==-1:
                    print(f"\nThe code lies between  100 to 499")
                elif clue==-2:
                    print(f"\nThe code lies between 500 to 999")
                else:
                    print(f"\nYou found a note with the number {clue} written on it indictaing the first digit!!")
                print(f"supicion gained ={suspicion1}")
                break
            else:
                choice=int(input("\nPlease enter a number between 1-6: "))

#scene2
        while True:
            investigate=input("\nDo you want to investigate a side room? (True or False)")                      #for the second scene( investigating side room)
            if investigate=="true" or investigate=="True":
                investigate=True
                break
            elif investigate=="false" or investigate=="False":
                investigate=False
                break
            else:
                print("\nPLEASE TYPE True or False")
        suspicion2, clue = side_room(investigate, code)
        print(f"\nsuspicion gained ={suspicion2}")                                                              # suspicion only from the second scene
        if clue == -1:
            print("\nYou found no clue.")
        elif clue >= 100:
            print(f"\nYou discovered the full code: {clue}")
        else:
            print(f"\nYou discovered the last digit: {clue}")
        suspicion=suspicion1+suspicion2                                                                         #total suspicion
        print(f"\nTotal suspicion={suspicion}")
#scene3
        suspicion3, cracked = crack_code(suspicion,code)
        suspicion = suspicion1+suspicion2+suspicion3
        print(f"\nTotal suspicion={suspicion}")
        print("\nGain 10 PROGRESS points to escape, but if your DANGER reaches 10, the guards catch you!")
        progress= escape(suspicion)
        if progress >= 10 and cracked == True:
            print("\nYou've WON!")
            break

        else:
            if progress < 10:
                print("\nYOU GOT CAUGHT")
            else:
                print("\nYou've escaped, but failed to crack the code")

            try_again = input("\nDo you want to try again? [Y/N]")

            if try_again == "Y" or try_again == "y":
                continue
            else:
                break

##start of game
DEBUG=False
print_signature()
name=input("What is your name?")
heist(name)