# Author: Eric Pauls
# Date: 6/9/2021
# Description: A class that represents the board game called Kuba. There are a variety of methods within the class
# that help make the game fully functional

class KubaGame:
    """
    class for the Kuba game. This is the only class in this program. This means the KubaGame class holds all the
    responsibilities of making the game operate properly.
    """

    def __init__(self, player_1, player_2):
        """
        init method for the board game. Takes in two tuples as arguments. The Tuples contain each player's name
        along with the color of marble they are playing with.
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self._player_1_name = player_1[0]
        self._player_1_color = player_1[1]
        self._player_2_name = player_2[0]
        self._player_2_color = player_2[1]
        self._current_turn = None  # will be tracked once the game is initiated
        self._next_turn = None  # will be tracked once the game is initiated
        self._winner = None  # will be tracked once the game is initiated
        self._player_1_captured = 0  # will be tracked once the game is initiated, shows number of reds captured
        self._player_2_captured = 0  # will be tracked once the game is initiated, shows number of reds captured
        self._previous_board = {}  # used to track if the current move is undoing prev move
        self._temp_board = {}  # moves happen on temp board. if current move is valid, board will become temp board
        self._board = {
            (0, 0): 'W', (0, 1): 'W', (0, 2): ' ', (0, 3): ' ', (0, 4): ' ', (0, 5): 'B', (0, 6): 'B',
            (1, 0): 'W', (1, 1): 'W', (1, 2): ' ', (1, 3): 'R', (1, 4): ' ', (1, 5): 'B', (1, 6): 'B',
            (2, 0): ' ', (2, 1): ' ', (2, 2): 'R', (2, 3): 'R', (2, 4): 'R', (2, 5): ' ', (2, 6): ' ',
            (3, 0): ' ', (3, 1): 'R', (3, 2): 'R', (3, 3): 'R', (3, 4): 'R', (3, 5): 'R', (3, 6): ' ',
            (4, 0): ' ', (4, 1): ' ', (4, 2): 'R', (4, 3): 'R', (4, 4): 'R', (4, 5): ' ', (4, 6): ' ',
            (5, 0): 'B', (5, 1): 'B', (5, 2): ' ', (5, 3): 'R', (5, 4): ' ', (5, 5): 'W', (5, 6): 'W',
            (6, 0): 'B', (6, 1): 'B', (6, 2): ' ', (6, 3): ' ', (6, 4): ' ', (6, 5): 'W', (6, 6): 'W',
        }  # board is a dictionary. key is tuple with coordinates of a tile, val is the contents of that game tile

    def print_board(self):
        """
        Prints the game board. Takes no parameters. This method is primarily being used for testing. So that the board
        moves can be visually seen
        """
        first = []  # visual for the board is a series of lists
        second = []
        third = []
        fourth = []
        fifth = []
        sixth = []
        seventh = []
        for _ in self._board.keys():
            if _[0] == 0:
                first.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 1:
                second.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 2:
                third.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 3:
                fourth.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 4:
                fifth.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 5:
                sixth.append(self._board[_])
        for _ in self._board.keys():
            if _[0] == 6:
                seventh.append(self._board[_])
        print(first)
        print(second)
        print(third)
        print(fourth)
        print(fifth)
        print(sixth)
        print(seventh)
        

    def get_current_turn(self):
        """get method for the current turn. Returns name of the player with the current turn."""
        return self._current_turn

    def get_next_turn(self):
        """get method for next turn. Returns the name of the player with the next turn"""
        return self._next_turn

    def get_winner(self):
        """get method for game winner. Returns None if no winner. Returns winners name if there is a winner"""
        return self._winner

    def get_captured(self, player_name):
        """get method that takes a player's name as a parameter and returns how many reds they have"""
        if player_name == self._player_1_name:
            return self._player_1_captured
        if player_name == self._player_2_name:
            return self._player_2_captured
        else:
            return False

    def get_marble(self, coordinates):
        """
        Returns the marble type located at the inputted coordinates. If space is empty, returns ' '.
        """
        if coordinates not in self._board:
            return False
        return self._board[coordinates]  # return the value for the given coordinate key

    def get_marble_count(self):
        """returns a tuple with a count of each marble on the board"""
        red = 0
        black = 0
        white = 0
        for space in self._board:  # loop through each key of the game board dictionary
            if self._board[space] == 'R':
                red += 1  # if value is a red marble, increase red count by one
            if self._board[space] == 'B':
                black += 1  # if value is a black marble, increase black count by one
            if self._board[space] == 'W':
                white += 1  # if value is a white marble, increase white count by one
        totals = (white, black, red)  # return count of all marbles
        return totals

    def win_check(self, playername):
        """
        Method is called each time a player scores. Takes in playername and updates the total count of red marbles
        that player has captured. If that player has captured 7, then the winner datamember is updated to
        show display that player is the winner.
        """
        if self._player_1_name is playername:  # if player one scored
            self._player_1_captured += 1  # increase their score by one
            if self._player_1_captured == 7:  # if player one has score of 7
                self._winner = self._player_1_name  # player one is the winner
        if self._player_2_name is playername:  # is player two scored
            self._player_2_captured += 1  # increase their score by one
            if self._player_2_captured == 7:  # if player two has a score of seven
                self._winner = self._player_2_name  # player two is the winner of the game
        return

    def undo_check(self):
        """ checks if the current move is undoing the prev move. If not, make board = temp board"""
        if self._temp_board == self._previous_board:    # if the move recreates player prev board
            return False    # return false
        else:
            for space in self._temp_board:    # update game board
                self._board[space] = self._temp_board[space]
            for space in self._previous_board:    # update prev board
                self._previous_board[space] = self._board[space]
            return True


    def turn_switcher(self):
        """method that switches the player current turn and next and next turn datamembers point to"""
        holder = self._current_turn
        self._current_turn = self._next_turn
        self._next_turn = holder

    def left_check(self, pieces_to_move, column, row, coordinates, playername):
        """if the move is the left, this method determines what needs to be done next"""
        if column != 6:  # if the column is not the furthest left column
            if self._temp_board[row, column + 1] != ' ':  # if the space in the immediate left column is not empty
                return False
        left = column - 1  # variable tracks the space in the column one to the left of the current piece
        for space in range(0, column):
            next_space = self._temp_board[(row, left)]  # tracks the space in the column one to the left of the current piece
            if next_space == ' ':  # if next space is empty
                self.move_left(pieces_to_move, left, row, coordinates)  # call move left method
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                return True
            if left == 0:
                if playername is self._player_1_name:
                    if next_space == self._player_1_color:
                        return False
                elif playername is self._player_2_name:
                    if next_space == self._player_2_color:
                        return False
                self.move_left(pieces_to_move, left, row, coordinates)
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                if next_space == 'R':
                    self.win_check(playername)
                return True
            else:
                pieces_to_move += 1
                left -= 1

    def move_left(self, pieces_to_move, left, row, coordinates):
        """
        Moves the pieces to the left. Takes in pieces_to_move (tracks number of pieces to move), left (starts on the
        leftmost piece being used and then backtracks in order to move the entire row), row (specifies what row
        the movement is taking place in), coordinates (used to clear the original space and store prior move in
        the last_move data member), playername, and direction. Both playername and direction are used to store prior
        move. Method modifies the board and the relevant last move variable
        """
        while pieces_to_move > 0:
            self._temp_board[(row, left)] = self._temp_board[row, left + 1]
            left += 1
            pieces_to_move -= 1
        self._temp_board[coordinates] = ' '

    def right_check(self, pieces_to_move, column, row, coordinates, playername):
        """if the move direction is right, then this method is called to determine what needs to be done"""
        if column != 0:
            if self._temp_board[row, column - 1] != ' ':
                return False
        right = column + 1
        for space in range(column, 6):
            next_space = self._temp_board[(row, right)]
            if next_space == ' ':
                self.move_right(pieces_to_move, right, row, coordinates)
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                return True
            if right == 6:
                if playername is self._player_1_name:
                    if next_space == self._player_1_color:
                        return False
                elif playername is self._player_2_name:
                    if next_space == self._player_2_color:
                        return False
                self.move_right(pieces_to_move, right, row, coordinates)
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                if next_space == 'R':
                    self.win_check(playername)
                return True
            else:
                pieces_to_move += 1
                right += 1

    def move_right(self, pieces_to_move, right, row, coordinates):
        """
        Moves the pieces to the right. Takes in pieces_to_move (tracks number of pieces to move), right (starts on the
        rightmost piece being used and then backtracks in order to move the entire row), row (specifies what row
        the movement is taking place in), coordinates (used to clear the original space and store prior move in
        the last_move data member), playername, and direction. Both playername and direction are used to store prior
        move. Method modifies the board and the relevant last move variable
        """
        while pieces_to_move > 0:
            self._temp_board[(row, right)] = self._temp_board[(row, right - 1)]
            right -= 1
            pieces_to_move -= 1
        self._temp_board[coordinates] = ' '

    def backwards_check(self, pieces_to_move, column, row, coordinates, playername):
        """if direction is B, this method determines what to do next"""
        if row != 0:    # if the row is not the first row
            if self._temp_board[row - 1, column] != ' ':    # if the preceding space is not empty
                return False    # return false
        backwards = row + 1    # helps track the piece one row down
        for space in range(row, 6):    # for each space between the tile being moved and the edge of the board
            next_space = self._temp_board[(backwards, column)]    # tracks piece next row down
            if next_space == ' ':  # if space is empty
                self.move_backwards(pieces_to_move, backwards, column, coordinates)    # move the pieces
                if self.undo_check() is False:    # if the move is reversing previous move, return false
                    return False
                self.turn_switcher()    # switch current and next turn data members
                return True
            if backwards == 6:    # if the next piece is the edge of the board
                if playername is self._player_1_name:    # if it is player one's turn
                    if next_space == self._player_1_color:    # if player is pushing their own piece off the board
                        return False
                elif playername is self._player_2_name:    # if it is player two's turn
                    if next_space == self._player_2_color:  # if player is pushing their own piece off the board
                        return False
                self.move_backwards(pieces_to_move, backwards, column, coordinates)    # move the pieces
                if self.undo_check() is False:    # if the move is reversing the previous move return false
                    return False
                self.turn_switcher()    # swap current turn and next turn
                if next_space == 'R':    # if a red piece was pushed off the board
                    self.win_check(playername)    # update the score and check if there is a winner
                return True
            else:
                pieces_to_move += 1
                backwards += 1

    def move_backwards(self, pieces_to_move, backwards, column, coordinates):
        """
        Moves the pieces backwards. Takes in pieces_to_move (tracks number of pieces to move), backwards (starts on the
        piece closest to the bottom that is being changed and then backtracks to move the entire column), column
        (specifies what column the movement is taking place in), coordinates (used to clear the original space and
        store prior move in the last_move data member), playername, and direction. Both playername and direction are
         used to store prior move. Method modifies the board and the relevant last move variable.
        """
        while pieces_to_move > 0:
            self._temp_board[(backwards, column)] = self._temp_board[(backwards - 1, column)]
            backwards -= 1
            pieces_to_move -= 1
        self._temp_board[coordinates] = ' '

    def forwards_check(self, pieces_to_move, column, row, coordinates, playername):
        """ if direction is F, then this method determines what to do next"""
        if row != 6:
            if self._temp_board[row + 1, column] != ' ':
                return False
        forwards = row - 1
        for space in range(0, row):
            next_space = self._temp_board[(forwards, column)]
            if next_space == ' ':
                self.move_forwards(pieces_to_move, forwards, column, coordinates)
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                return True
            if forwards == 0:
                if playername is self._player_1_name:
                    if next_space == self._player_1_color:
                        return False
                elif playername is self._player_2_name:
                    if next_space == self._player_2_color:
                        return False
                self.move_forwards(pieces_to_move, forwards, column, coordinates)
                if self.undo_check() is False:
                    return False
                self.turn_switcher()
                if next_space == 'R':
                    self.win_check(playername)
                return True
            else:
                pieces_to_move += 1
                forwards -= 1

    def move_forwards(self, pieces_to_move, forwards, column, coordinates):
        """
        Moves the pieces forwards. Takes in pieces_to_move (tracks number of pieces to move), forwards (starts on the
        piece closest to the top that is being changed and then backtracks to move the entire column), column
        (specifies what column the movement is taking place in), coordinates (used to clear the original space and
        store prior move in the last_move data member), playername, and direction. Both playername and direction are
         used to store prior move. Method modifies the board and the relevant last move variable.
        """
        while pieces_to_move > 0:
            self._temp_board[(forwards, column)] = self._temp_board[(forwards + 1, column)]
            forwards += 1
            pieces_to_move -= 1
        self._temp_board[coordinates] = ' '

    def make_move(self, playername, coordinates, direction):
        """
        Method to allow player to make a move on the board. Takes in the playername, coordinates of space
        being moved, and the direction of the move. There are a number of if statements that help determine if
        the move is valid. If the move is determined to be valid, then the method sets up variables specific
        to the direction (left, right, backwards, forwards) and passes those variables to the relevant move
        variable. If a red marble is to be pushed off the board, then the check win method is called.
        """
        if coordinates not in self._board:  # if coordinates are not valid
            return False
        if direction not in 'LRFB':  # if direction is not valid
            return False
        if self._winner is not None:  # if the game has already been won
            return False
        if playername is self._player_1_name:
            if self._board[coordinates] is not self._player_1_color:
                return False  # if player one does not have a marble in the square they are trying to move, False
        if playername is self._player_2_name:
            if self._board[coordinates] is not self._player_2_color:
                return False  # if player two does not have a marble in the square they are trying to move, False
        if self._current_turn is None:  # if its the first move of the game
            self._current_turn = playername  # set current turn to the player making the first move
            if self._current_turn is self._player_1_name:  # set next turn
                self._next_turn = self._player_2_name  # next turn is player 2 if player one is current turn
            else:
                self._next_turn = self._player_1_name  # next turn is player 1 if player 2 is current turn
        row = coordinates[0]  # specifies which row the piece to be moved is on
        column = coordinates[1]  # specifies which column the piece to be moved is on
        pieces_to_move = 1  # variable tracks how many pieces needed to be moved for the current turn
        if playername is not self._current_turn:  # if the player trying to make a move is not current turn
            return False
        # set self temp board to self._board and then proceed to make move on temp board
        self._temp_board = self._board
        for space in self._board:
            self._temp_board[space] = self._board[space]
        if direction == 'L':  # if direction is left, initiate left_check
            return self.left_check(pieces_to_move, column, row, coordinates, playername)
        if direction == 'R':  # if direction is right, initiate right_check
            return self.right_check(pieces_to_move, column, row, coordinates, playername)
        if direction == 'B':  # if direction is backwards, initiate backwards check
            return self.backwards_check(pieces_to_move, column, row, coordinates, playername)
        if direction == 'F':  # if direction is forwards, initiate forwards check
            return self.forwards_check(pieces_to_move, column, row, coordinates, playername)









