import random
from numpy import *

def win(arr):
    if (arr[0][0] == arr[0][1] and arr[0][1] == arr[0][2] and arr[0][0] != "5"):
        return True;
    elif (arr[0][0] == arr[1][0] and arr[1][0] == arr[2][0] and arr[0][0] != "5"):
        return True;
    elif (arr[2][0] == arr[2][1] and arr[2][1] == arr[2][2] and arr[2][0] != "5"):
        return True;
    elif (arr[0][2] == arr[1][2] and arr[1][2] == arr[2][2] and arr[2][2] != "5"):
        return True;
    elif (arr[0][0] == arr[1][1] and arr[1][1] == arr[2][2] and arr[0][0] != "5"):
        return True;
    elif (arr[2][0] == arr[1][1] and arr[1][1] == arr[2][0] and arr[2][0] != "5"):
        return True;
    elif (arr[1][0] == arr[1][1] and arr[1][1] == arr[1][2] and arr[1][0] != "5"):
        return True;
    elif (arr[0][1] == arr[1][1] and arr[1][1] == arr[2][1] and arr[1][1] != "5"):
        return true;
    return False;

def show(arr):
    for row in range(3):
        for col in range(3):
            print(arr[row][col],end=" ")
        print()


chances = 9
tic_tac = array([['5','5','5'],['5','5','5'],['5','5','5']])
playerName = input("Player Enter Your Name: ")
player = 'X'
computer = '0'
while True:
    x = int(input(playerName+" enter the X-ordinate"))
    y = int(input(playerName+" enter the Y-ordinate"))
    if x >= 0 and x < 3 and y >= 0 and y < 3 and tic_tac[x][y] == '5':
        tic_tac[x][y] = player
        chances -= 1
    elif x < 0 and x >= 3 and y < 0 and y >= 3:
        print("Co-ordinate out of Range")
        continue
    else:
        print("The Position is Already Occupied")
        continue
    show(tic_tac)
    if chances == 0:
        print("Draw")
        break
    if win(tic_tac):
        print(playerName+" Wins")
        break
    print("------------")
    print("------------")
    print("Computer's Chance To Play")
    while True:
        row = int(random.random()*10)%3
        col = int(random.random()*10)%3
        if tic_tac[row][col] == '5':
            tic_tac[row][col] = computer
            chances -= 1
            show(tic_tac)
            if win(tic_tac):
                print("Computer Wins")
                break
            if chances == 0:
                print("Draw")
                break
        else:
            continue
    #if win(tic_tac) or chances == 0:
        break