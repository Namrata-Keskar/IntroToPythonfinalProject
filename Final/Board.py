import random
import os
import sys

class Board():
    board = [' '] * 10

    def showIntro(self):
        ans = 'no ans'
        while (ans.startswith('Y') != True) or (ans.startswith('N') != True):
            print('Do you want to see the instructions? Please type Y for yes or N for no.')
            ans = input()
            ans = ans.upper()
            if ans.startswith('Y'):
                print()
                print('Tic Tac Toe is a 2 player game in which the players take turns marking a 3x3 grid. One player will choose to mark their spaces with the letter /"X/" and the other player will use the letter /"O/". The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.')
                return ''
            elif ans.startswith('N'):
                return ''

    def drawBoard(self):
        # This function prints out the board that it was passed.
        # "board" is a list of 10 strings representing the board (ignore index 0)
        
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        return random.randint(0, 1) 

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        #return input().lower().startswith('y')

    def isWinner(self, le):
        self.le = le
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == self.le and self.board[8] == self.le and self.board[9] == self.le) or # across the top
        (self.board[4] == self.le and self.board[5] == self.le and self.board[6] == self.le) or # across the middle
        (self.board[1] == self.le and self.board[2] == self.le and self.board[3] == self.le) or # across the bottom
        (self.board[7] == self.le and self.board[4] == self.le and self.board[1] == self.le) or # down the left side
        (self.board[8] == self.le and self.board[5] == self.le and self.board[2] == self.le) or # down the middle
        (self.board[9] == self.le and self.board[6] == self.le and self.board[3] == self.le) or # down the right side
        (self.board[7] == self.le and self.board[5] == self.le and self.board[3] == self.le) or # diagonal
        (self.board[9] == self.le and self.board[5] == self.le and self.board[1] == self.le)) # diagonal
     #def getBoardCopy(self, board):
     #   self.board = board
     #   # Make a duplicate of the board list and return it the duplicate.
     #   dupeBoard = []

     #   for i in self.board:
     #       dupeBoard.append(i)

        # return dupeBoard
    def isSpaceFree(self, move):
        self.move = move
        #self.getPlayer1Move(self)
        #self.getPlayer2Move(self)
        # Return true if the passed move is free on the passed board.
        return self.board[self.move] == ' '

    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True
