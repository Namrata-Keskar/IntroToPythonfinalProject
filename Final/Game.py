from Player import Player
from Board import Board
import os
import sys

board = 0
board = Board() 
player1 = Player(1, board)
player2 = Player(2, board)

gameSetUp = True



while True:
   
    while gameSetUp:
        print('Welcome to Tic Tac Toe!')
        board.showIntro()

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

        currentPlayer = firstPlayer

        #draw the board
        os.system('cls')
        board.drawBoard()

        gameSetUp = False
        gameIsPlaying = True

    while gameIsPlaying:
        #current players makes the move
        currentPlayer.makeMove()

        #draw the board
        os.system('cls')
        board.drawBoard()

        #check if chosen player is winner or board is fill... Game Over
        if board.isWinner(currentPlayer.letter):
            print('Hooray! ' + currentPlayer.name + ' won the game!')
            gameIsPlaying = False
            #break
        else:
            if board.isBoardFull():
                print('The game is a tie!')
                gameIsPlaying = False
                #break
        
        #now second player becomes the chosen one
        if(currentPlayer == firstPlayer):
            currentPlayer = secondPlayer
        else:
            currentPlayer = firstPlayer

    while gameIsPlaying == False:
        answer = board.playAgain()  
        if answer == True:
            os.system('cls')
            gameSetUp = True
            gameIsPlaying = True
            continue
        elif answer == False:
            sys.exit()