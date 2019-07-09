#This second chunk is a version that I tried to make with a Player class and Board(Player) class

import random

class Player:
    def playerName(self):
        print('What name would you like for your player?')
        name = input()
        return name
    def makeMove(self, board, letter, move):
        self.board[self.move] = self.letter
    def isWinner(self, bo, le):
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
    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return self.board[self.move] == ' '
    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(self.board, int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

class Board(Player):
    def drawBoard(board):
        # This function prints out the board that it was passed
        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')
    def whoGoesFirst(self, player1, player2):
        #Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return self.player1
        else:
            return self.player2
    def inputPlayerLetter(self, firstPlayer):
        # Lets the player type which letter they want to be.
        # Returns a list with the player's letter as the first item, and the computer's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print(firstPlayer + ' will play first.')
            print('Do you want to be X or O?')
            letter = input().upper()
        # the first element in the tuple is the player1's letter, the second is the player2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')
    def getBoardCopy(board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)

        return dupeBoard
    def isBoardFull(board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if isSpaceFree(board, i):
                return False
        return True

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    player1 = Player()
    player2 = Player()
    gameBoard = Board()
    theBoard = [' '] * 10
    #playerLetter, computerLetter = inputPlayerLetter()
    name1 = player1.playerName()
    name2 = player2.playerName()
    turn = gameBoard.whoGoesFirst(player1, player2)
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player 1':
            # Player1's turn.
            gameBoard.drawBoard(theBoard)
            move = player1.getPlayerMove(theBoard)
            player1.makeMove(theBoard, player1Letter, move)

            if player1.isWinner(theBoard, player1Letter):
                gameBoard.drawBoard(theBoard)
                print('Hooray! ' + name1 + ' have won the game!')
                gameIsPlaying = False
            else:
                if gameBoard.isBoardFull(theBoard):
                    gameBoard.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'
        else:
            # Player2's turn.
            move = player2.getPlayerMove(theBoard)
            makeMove(theBoard, player2Letter, move)

            if isWinner(theBoard, player2Letter):
                gameBoard.drawBoard(theBoard)
                print('Hooray! ' + name2 + ' have won the game!')
                gameIsPlaying = False
            else:
                if gameBoard.isBoardFull(theBoard):
                    gameBoard.drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player 2'

    if not gameBoard.playAgain():
        break