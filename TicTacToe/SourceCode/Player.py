from Board import Board

# This class is a Player class that includes all the functions related to a player.

class Player():
    name = 'NoName'
    letter = ''
    playerNumber = 0
    board = 0

    def __init__(self, playerNumber, bo):
        # Initiaizes the player number and gives the player access to the board.
        self.playerNumber = playerNumber
        self.board = bo
        
    def assignPlayerName(self):
        # This function allows the players to set a character name for their player.
        # the player is address wiht this name throughout the game.
        print('What name would you like for player ' + str(self.playerNumber) + '?')
        self.name = input()
        print()

    def chooseLetter(self):
        self.letter = ' '
        # Lets the player type which letter they want to be.
        # Returns a the player's choice
        print(self.name + ' has been chosen to go first.')
        while not (self.letter == 'X' or self.letter == 'O'):
            print('Does ' + self.name + ' want to be X or O?')
            self.letter = input().upper()

        return self.letter

    def makeMove(self):
        # This function asks the player what move they want to make and checks if is a valid move.
        move = ' '
        while (move not in '1 2 3 4 5 6 7 8 9'.split()) or (not self.board.isSpaceFree(int(move))):
            print(self.name + ', what is your move? (1-9)')
            move = input()
            if move not in '1 2 3 4 5 6 7 8 9'.split():
                print('Please enter a number between 1 and 9.')
            elif not self.board.isSpaceFree(int(move)):
                print('That space is already filled, please type another move.')
        self.board.board[int(move)] = self.letter
    
   
