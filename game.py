import random
playerscore=0
computerscore=0
Game_elements=["Rock","Paper","Scissor"]
Playername=input("Enter your Name:")
print(f"{Playername},lets start the game!")
print("-------TOTAL 5 ROUND-------")

round = 0
while round < 5:
    print("Round:", round + 1)
    print("Pick one:\n 1.Rock \n 2.Paper \n 3.Scissor \n 4.Quit Game")
    playerchoice = int(input())
    computerchoice =random.choice(Game_elements)

    game_elements = {1: "Rock", 2: "Paper", 3: "Scissor"}

    if playerchoice == 1:
        playerchoice = "Rock"
        print(f"Your choice is {playerchoice} and computer choice is {computerchoice}")
        if playerchoice == computerchoice:
            print("Match Draw!")
        elif computerchoice == "Scissor":
            playerscore +=1
            print(f"Rock smashes Scissor,{Playername} Wins!")
        else:
            computerscore +=1
            print("Paper covers the rock,Computer Wins!")
    elif playerchoice == 2:
        playerchoice = "Paper"
        print(f"Your choice is {playerchoice} and computer choice is {computerchoice}")
        if playerchoice == computerchoice:
            print("Match Draw!")
        elif computerchoice == "Rock":
            playerscore = playerscore+1
            print(f"Paper covers the rock,{Playername} Wins!")
        else:
            computerscore = computerscore+1
            print("Scissor cuts the Paper,Computer Wins!")
    elif playerchoice == 3:
        playerchoice = "Scissor"
        print(f"Your choice is {playerchoice} and computer choice is {computerchoice}")
        if playerchoice == computerchoice:
            print("Match Draw!")
        elif computerchoice == "Paper":
            playerscore +=1
            print(f"Scissor cuts the paper,{Playername} Wins!")
        else:
            computerscore +=1
            print("Rock breaks the scissor,Computer Wins!")

    elif playerchoice == 4:
        print("Game Over")
        quit()

    else:
        print("Choose valid choices")

    round += 1



print("-----------------------------------------")
print("Final Result")
if playerscore<computerscore:
    print("Computer wins the Trophy")
elif playerscore==computerscore:
    print("Match draw")
else:
    print(f"{Playername} Wins the Trophy")
print("-----Game Over------")
print(f"{Playername} score:{playerscore}\nComputer score:{computerscore}")
