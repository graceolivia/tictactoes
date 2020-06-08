# tic tac toe from scratch #
import random
import cs50

board = {'1': ' ', '2': ' ', '3': ' ',
        '4': ' ', '5': ' ', '6': ' ',
        '7': ' ', '8': ' ', '9': ' '}

def welcome():
    print("Welcome to Tic Tac Toe. Select your input by giving the board position you wish to mark, as shown below:")
    print("1|2|3")
    print('-+-+-')
    print("4|5|6")
    print('-+-+-')
    print("7|8|9")


def printboard(b):
    print(b['1'] + "|" + b['2'] + "|" + b['3'])
    print('-+-+-')
    print(b['4'] + "|" + b['5'] + "|" + b['6'])
    print('-+-+-')
    print(b['7'] + "|" + b['8'] + "|" + b['9'])

def moveChecker(i, value):
    #get values in dicts
    space = board.get(i)
    if space == ' ':
        board.update({i: value})
        return(1)
    else:
        return(0)


def move(player):
    move = 0
    while True:
        x = input(player + ' moves:')
        try:
            move = int(x)
        except ValueError:
            print("Please enter a whole number between 1 and 9")
            continue
        if (move > 0) and (move < 10):
            #to check if it's a free space
            check = moveChecker(x, player)
            if check == 1:
                return
            if check == 0:
                print('please pick an open space')
        else:
            print("Enter board number between 1 and 9")

def computerMove(player):
    while True:
        a = random.randint(1, 9)
        move = str(a)
        space = board.get(move)
        if space == ' ':
            board.update({move: player})
            break
    return

def winChecker(i):
    if (board['1'] == i) and (board['2'] == i) and (board['3'] == i):
        return 1
    elif (board['4'] == i) and (board['5'] == i) and (board['6'] == i):
        return 1
    elif (board['7'] == i) and (board['8'] == i) and (board['9'] == i):
        return 1
    elif (board['1'] == i) and (board['4'] == i) and (board['7'] == i):
        return 1
    elif (board['2'] == i) and (board['5'] == i) and (board['8'] == i):
        return 1
    elif (board['3'] == i) and (board['6'] == i) and (board['9'] == i):
        return 1
    elif (board['1'] == i) and (board['5'] == i) and (board['9'] == i):
        return 1
    elif (board['3'] == i) and (board['5'] == i) and (board['7'] == i):
        return 1
    return 0


def pvp():
    welcome()
    moves = 0
    for a in "XOXOXOXOX":
        move(a)
        moves += 1
        printboard(board)
        if moves > 4:
            if (winChecker(a) == 1):
                print(a + " wins!")
                return
    print("It's a draw.")

def pvc():
    welcome()
    moves = 0
    for a in "XOXOXOXOX":
        if a == "X":
            move(a)
            moves += 1
            printboard(board)
        if a == "O":
            print("Computer's move:")
            computerMove(a)
            moves += 1
            printboard(board)
        if moves > 4:
            if (winChecker(a) == 1):
                print(a + " wins!")
                return

    print("It's a draw.")
    return


def gameStart():
    while True:
        x = input("Type 1 for player vs player, Type 2 for player vs computer: ")
        if x == '1':
            pvp()
            return
        if x == '2':
            pvc()
            return
        else:
            continue

gameStart()