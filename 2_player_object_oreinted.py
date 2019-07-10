# Object oriented design
import random
import os
import sys

class Board():
    def showIntro(self):
        self.ans = 'no ans'
        while (self.ans.startswith('Y') != True) or (self.ans.startswith('N') != True):
            print('Do you want to see the instructions? Please type Y for yes or N for no.')
            self.ans = input()
            self.ans = self.ans.upper()
            if self.ans.startswith('Y'):
                print()
                print('Tic Tac Toe is a 2 player game in which the players take turns marking a 3x3 grid. One player will choose to mark their spaces with the letter /"X/" and the other player will use the letter /"O/". The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.')
                return ''
            elif self.ans.startswith('N'):
                return ''
    def drawBoard(self, board):
        self.board = board
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

    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Does ' + board.turn + ' want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player's letter, the second is the computer's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        self.turn = ''
        if random.randint(0, 1) == 0:
            return player1.name
        else:
            return player2.name
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        self.ans = ''
        print('Do you want to play again? (yes or no)')
        #return input().lower().startswith('y')
    def isWinner(self, bo, le):
        self.bo = bo
        self.le = le
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.bo[7] == self.le and self.bo[8] == self.le and self.bo[9] == self.le) or # across the top
        (self.bo[4] == self.le and self.bo[5] == self.le and self.bo[6] == self.le) or # across the middle
        (self.bo[1] == self.le and self.bo[2] == self.le and self.bo[3] == self.le) or # across the bottom
        (self.bo[7] == self.le and self.bo[4] == self.le and self.bo[1] == self.le) or # down the left side
        (self.bo[8] == self.le and self.bo[5] == self.le and self.bo[2] == self.le) or # down the middle
        (self.bo[9] == self.le and self.bo[6] == self.le and self.bo[3] == self.le) or # down the right side
        (self.bo[7] == self.le and self.bo[5] == self.le and self.bo[3] == self.le) or # diagonal
        (self.bo[9] == self.le and self.bo[5] == self.le and self.bo[1] == self.le)) # diagonal
     #def getBoardCopy(self, board):
     #   self.board = board
     #   # Make a duplicate of the board list and return it the duplicate.
     #   dupeBoard = []

     #   for i in self.board:
     #       dupeBoard.append(i)

        # return dupeBoard
    def isSpaceFree(self, board, move):
        self.board = board
        self.move = move
        #self.getPlayer1Move(self)
        #self.getPlayer2Move(self)
        # Return true if the passed move is free on the passed board.
        return self.board[self.move] == ' '
    def isBoardFull(self, board):
        self.board = board
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(self.board, i):
                return False
        return True
     


class Player(Board):
    def playerName(self):
        print()
        print('What name would you like for your player?')
        self.name = ''

    def makeMove(self, board, letter, move):
        self.board = board
        self.letter = letter
        self.move = move
        self.board[self.move] = self.letter
    
    def getPlayer1Move(self, board):
        #self.isSpaceFree = self.isSpaceFree(board)
        self.board = board
        # Let the player 1 type in his move.
        move = ' '
        while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (not self.isSpaceFree(self.board, int(move))):
            print(player1.name + ', what is your move? (1-9)')
            move = input()
            if move not in '1 2 3 4 5 6 7 8 9'.split():
                print('Please enter a number between 1 and 9.')
            elif not self.isSpaceFree(self.board, int(move)):
                print('That space is already filled, please type another move.')
        return int(move)
    def getPlayer2Move(self, board, player2Letter):
        #self.isSpaceFree = self.isSpaceFree(board)
        self.board = board
        self.player2Letter = player2Letter
        #if self.player2Letter == 'X':
         #   player1Letter = 'O'
        #else:
         #   player1Letter = 'X'
        
        # Let the player 2 type in his move.
        move = ' '
        while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (not self.isSpaceFree(self.board, int(move))):
            print(player2.name + ', what is your move?(1-9)')
            move = input()
            if move not in '1 2 3 4 5 6 7 8 9'.split():
                print('Please enter a number between 1 and 9.')
            elif not self.isSpaceFree(self.board, int(move)):
                print('That space is already filled, please type another move.')
        return int(move)



print('Welcome to Tic Tac Toe!')
player1 = Player()
player2 = Player()
board = Board() 



while True:
    # Reset the board
    board.showIntro()

    theBoard = [' '] * 10
    player1.playerName()
    player1.name = input()
    player2.playerName()
    player2.name = input()
    board.turn = board.whoGoesFirst()
    print()
    print(board.turn + ' will go first.')
    player1Letter, player2Letter = board.inputPlayerLetter()
    
    gameIsPlaying = True

    while gameIsPlaying:
        if board.turn == player1.name:
            # Player 1's  turn.
            os.system('cls')
            board.drawBoard(theBoard)
            move = player1.getPlayer1Move(theBoard)
            player1.makeMove(theBoard, player1Letter, move)

            if board.isWinner(theBoard, player1Letter):
                board.drawBoard(theBoard)
                print('Hooray! ' + player1.name + ' won the game!')
                gameIsPlaying = False
            else:
                if board.isBoardFull(theBoard):
                    board.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    board.turn = player2.name

        else:
            # Player 2's turn.
            os.system('cls')
            board.drawBoard(theBoard)
            move = player2.getPlayer2Move(theBoard, player2Letter)
            player2.makeMove(theBoard, player2Letter, move)

            if board.isWinner(theBoard, player2Letter):
                board.drawBoard(theBoard)
                print('Hooray! ' + player2.name + ' won the game.')
                gameIsPlaying = False
            else:
                if board.isBoardFull(theBoard):
                    board.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    board.turn = player1.name

    while board.ans != 'y' or board.ans != 'n':
        board.playAgain()
        board.ans = input().lower()
        if board.ans == 'y':
            os.system('cls')
            break
        elif board.ans == 'n':
            sys.exit()
     