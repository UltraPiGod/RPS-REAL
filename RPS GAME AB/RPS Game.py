import sys
from random import randint

cpi = randint(0,2)

options = ["Rock", "Paper", "Scissors"]

person = 0
api = 0
player = " "
personChoice = 0

player = input("Enter your worthless name:").title()
while not player.isalpha():
    print("Not a valid name")
    player = input("Enter your worthless name:").title()

while True:
    try:
        file = open(player + ".txt", "r")
        file.close()
        break
    except FileNotFoundError:
        file = open(player + ".txt", "w+")
        file.write("0")
        file.close()

#Name only (No Numbers)       


def startGame():
    global person
    global api
    global player
    cpig = options[randint(0,2)]
            
    print("Hello " + player +"\n "+ "You dare challenge me? Well lets see what you've got!")
    playerGuess = input("I've got my guess, so you go, Rock, Paper, or Scissors?").title()
    print("Computer = " + str(api))
    print("You = " + str(person))
   
    if (playerGuess  == cpig):
        print("You Tied... This time")
        startLoop()
        
    elif (playerGuess  == "Rock" or "r"):
        if (cpig == "Paper"):
            print("You Lose, HA! garbage.")
            api += 1
            startLoop()
    
        else:
            print("You Win!")
            person += 1
            startLoop()

    elif (playerGuess == "Paper" or "p"):
        if (cpig == "Scissors"):
            print("You Lose, HA! garbage.")
            api += 1
            startLoop()
        
        else:
            print("You Win!")
            person += 1
            startLoop()

    elif (playerGuess == "Scissors" or "r"):
        if(cpig == "Rock"):
            print("You Lose, HA! garbage.")
            api += 1
            startLoop()
         
        else:
            print("You Win!")
            person += 1
            startLoop()
          
    else:
        print("That's not one of the choices!")
        startLoop()

#top10 function
def top10():
    numbers_of_top10 = []
    names = []
    global player
    file = open(player + ".txt", "r")
    win = [line.strip() for line in file]
    file.close()
    while True:
        try:
            file = open("top10.txt", "r")
            top10 = [line.strip() for line in file]
            file.close()
            break
        except FileNotFoundError:
            file = open("top10.txt", "w+")
            file.write("TylerSee 20 wins\nNijelheeper 12 wins\nCameronBee 6 wins")
            file.close()
            file = open("top10.txt", "r")
            top10 = [line.strip() for line in file]
            file.close()

    for i in range(len(top10)):
        element = top10[i]
        wins = ""
        for letter in element:
            if not letter.isalpha() and letter != " ":
                wins += letter
        numbers_of_top10.append(wins)

    for i in range(len(top10)):
        element = top10[i]
        name = ""
        for letter in element:
            if letter != " ":
                name += letter
            else:
                names.append(name)
                break

    for i in range(len(names)):
        if names[i] == player:
            del top10[i]
            del numbers_of_top10[i]

    for i in range(len(numbers_of_top10)):
        if int(win[0]) > int(numbers_of_top10[i]):
            top10.insert(i,player+" "+win[0]+" wins")
            break

    if len(top10) > 10:
        del top10[len(top10) - 1]
    elif len(top10) < 10 and int(win[0]) < int(len(numbers_of_top10)-1):
        top10.append(player+" "+win[0]+" wins")
    else:
        pass

    new_top10 = "\n".join(top10)

    print(new_top10)
    
    file = open("top10.txt", "w+")
    file.write(new_top10)
    file.close()

#The loop function
def startLoop():
    global person
    global api
    cpig = options[randint(0,2)]
    playerGuess = input("I've got my guess again, so you go, Rock, Paper, or Scissors?").title()
   
    if (playerGuess  == cpig):
        print("You Tied... This time")
        
        
    elif (playerGuess  == "Rock" or "r"):
        if (cpig == "Paper"):
            print("You Lose, HA! garbage.")
            api += 1
         
        else:
            print("You Win!")
            person += 1

    elif (playerGuess == "Paper" or "p"):
        if (cpig == "Scissors"):
            print("You Lose, HA! garbage.")
            api += 1
         
        else:
            print("You Win!")
            person += 1

    elif (playerGuess == "Scissors" or "s"):
        if(cpig == "Rock"):
            print("You Lose, HA! garbage.")
            api += 1
        
        else:
            print("You Win!")
            person += 1

    else:
        print("That's not one of the choices!")
        startLoop()

                
#cpig is cpiguess
while player.title():
    startGame()
    print("Computer = " + str(api))
    print("You = " + str(person))
    break

while person < 5 and api < 5:
    startLoop()
    print("Computer = " + str(api))
    print("You = " + str(person))
    
    if(person == 5):
        file = open(player+ ".txt", "r")
        win = [line.strip() for line in file]
        file.close()
        wins = int(win[0])
        wins += 1
        file = open(player + ".txt", "w+")
        file.write(str(wins))
        file.close()

        top10()
        
        personChoice = input("You won five times, NICE!!!" + "\n" + "Do you wanna play again?"+ "\n" + "Yes or No?").title()
        if(personChoice == "Yes"):
            startGame()
            person = 0
            api = 0
            cpi = 0
        elif(personChoice == "No"):
            sys.exit(0)

    if(api == 5):
        print("I won five times, good run!")
        personChoice = input("I won five times, NICE!!!" + "\n" + "Do you wanna play again?"+ "\n" + "Yes or No?").title()
        if(personChoice == "Yes"):
            startGame()
            person = 0
            api = 0
            cpi = 0
        elif(personChoice == "No"):
            sys.exit(0)

startGame()

