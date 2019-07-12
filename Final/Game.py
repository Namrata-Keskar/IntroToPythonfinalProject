from Player import Player
from Board import Board
import os
import sys

print('Welcome to Tic Tac Toe!')

board = 0
board = Board() 
player1 = Player(1, board)
player2 = Player(2, board)

player1.assignPlayerName()
player2.assignPlayerName()

firstPlayer = player1
secondPlayer = player2

firstPlayerNumber = board.whoGoesFirst()
if(firstPlayerNumber == 1):
    firstPlayer = player2
    secondPlayer = player1

secondPlayer.letter = 'X'
letterChosen = firstPlayer.chooseLetter()
if(letterChosen == 'X'):
    secondPlayer.letter = 'O'

gameIsPlaying = True

currentPlayer = firstPlayer

#draw the board
board.drawBoard()

while gameIsPlaying:

    #current players makes the move
    currentPlayer.makeMove()

    #draw the board
    board.drawBoard()

    #check if chosen player is winner or board is fill... Game Over
    if board.isWinner(currentPlayer.letter):
        print('Hooray! ' + player1.name + ' won the game!')
        break
    else:
        if board.isBoardFull():
            print('The game is a tie!')
            break
        
    #now second player becomes the chosen one
    if(currentPlayer == firstPlayer):
        currentPlayer = secondPlayer
    else:
        currentPlayer = firstPlayer

while board.ans != 'y' or board.ans != 'n':
    board.playAgain()
    board.ans = input().lower()
    if board.ans == 'y':
        os.system('cls')
        break
    elif board.ans == 'n':
        sys.exit()

    