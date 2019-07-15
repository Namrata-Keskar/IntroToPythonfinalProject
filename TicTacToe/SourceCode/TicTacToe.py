from Player import Player
from Board import Board
import os
import sys


class TicTacToe():
    board = Board()
    player1 = Player(1, board)
    player2 = Player(2, board)

    def Play(self):
        gameSetUp = True

        while True:

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

            while gameIsPlaying == False:
                answer = self.board.playAgain()
                if answer == True:
                    os.system('cls')
                    gameSetUp = True
                    gameIsPlaying = True
                    continue
                elif answer == False:
                    sys.exit()


game = TicTacToe()
game.Play()

