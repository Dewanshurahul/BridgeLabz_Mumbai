#Tracking the position of a gambler during a game
#i.e Number of wins
# Number of Times Played
# And Providing the Percentage of wins during the game
import random
stake = int(input("Enter the Stake you want to put: "))
goal = int(input("Enter the Goal you want to reach: "))
win = 0
desiredChances = int(input("Enter how many times you wnat to Play: "))
numberOfBets = 0
if goal <= 0 or stake <= 0 or desiredChances <= 0:
    print("Invalid Input")
else:
    while numberOfBets <= desiredChances and stake != 0 and stake != goal:
        bet = random.random()
        if bet > 0.5:
            win += 1
            stake += 1
        else:
            stake -= 1
        numberOfBets += 1
    if stake == goal:
        print("Congratulations")
    else:
        print("Better Luck Next Time.")
    print("Stake Left After Game is: " + str(stake))
    print("Total wins are: " + str(win))
    print("Total times Played: " + str(numberOfBets))
    print("Percentage win is: " + str(int(win / numberOfBets * 100)) + "%")