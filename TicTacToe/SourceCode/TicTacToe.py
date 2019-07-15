from Player import Player
from Board import Board
import os
import sys

# This class is a TicTacToe class that contains the Play function that runs the actual game.

class TicTacToe():
    # One board object and two player objects are created for the game.
    board = Board()
    player1 = Player(1, board)
    player2 = Player(2, board)

    def Play(self):
        gameSetUp = True

        while True:
            # This while loop runs when the game need to display the introduction of game.
            # This includes the instructions, choosing player names, randomly assigning a player to go first
            # and allowing the first player to choose their letter.
            while gameSetUp:
                print('Welcome to Tic Tac Toe!')
                self.board.showIntro()

                self.player1.assignPlayerName()
                self.player2.assignPlayerName()

                firstPlayer = self.player1
                secondPlayer = self.player2
                firstPlayerNumber = self.board.whoGoesFirst()
                if(firstPlayerNumber == 1):
                    firstPlayer = self.player2
                    secondPlayer = self.player1

                secondPlayer.letter = 'X'
                letterChosen = firstPlayer.chooseLetter()
                if(letterChosen == 'X'):
                    secondPlayer.letter = 'O'

                currentPlayer = firstPlayer

                # draw the board
                os.system('cls')
                self.board.drawBoard()

                gameSetUp = False
                gameIsPlaying = True

            while gameIsPlaying:
                # This while loop runs when the actual game is being played and when the players are making
                # their moves.

                # current players makes the move
                currentPlayer.makeMove()

                # draw the board
                os.system('cls')
                self.board.drawBoard()

                # check if chosen player is winner or board is fill... Game Over
                if self.board.isWinner(currentPlayer.letter):
                    print('Hooray! ' + currentPlayer.name + ' won the game!')
                    gameIsPlaying = False
                    #break
                else:
                    if self.board.isBoardFull():
                        print('The game is a tie!')
                        gameIsPlaying = False
                        #break

                # now second player becomes the chosen one
                if(currentPlayer == firstPlayer):
                    currentPlayer = secondPlayer
                else:
                    currentPlayer = firstPlayer

            # This while loop is called when the game is over.
            # It allows the player to play again or exits the program.
            while gameIsPlaying == False:
                answer = self.board.playAgain()
                if answer == True:
                    os.system('cls')
                    gameSetUp = True
                    gameIsPlaying = True
                    continue
                elif answer == False:
                    sys.exit()


# A object of the TicTacToe class is created, and they Play function of that object is called.
game = TicTacToe()
game.Play()

