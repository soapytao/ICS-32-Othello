# Sophia Tao, 20293428, stao3@uci.edu

class InvalidMoveError(Exception):
    '''Raised when an invalid move is made'''
    pass

class GameOverError(Exception):
    '''Raised when an attempt to make a move is made after the game is over'''
    pass


class GameState:

    def __init__(self, rows:int, cols:int, first_turn: int, how_to_win: str, initial_board:list):
        
        #specified dimensions of the board
        self._rows = rows
        self._cols = cols

        #specified first player
        self._turn = first_turn

        #specified win conditions
        self._how_to_win = how_to_win

        #initial board
        self._board = initial_board

        #pieces
        self._black = 1
        self._white = 2
        self._empty = 0

        #scoreboard
        self._blackscore = 0
        self._whitescore = 0

    def get_turn(self):
        '''Returns which player's turn it is'''
        return self._turn

    def get_board(self):
        '''Returns the current board'''
        return self._board

    def switch_turn(self):
        '''Returns the opposite player's turn'''
        if self._turn == self._black:
            return self._white
        else:
            return self._black
        
    def move(self, choice: list):
        '''Places the current player's piece in the specified cell if applicable'''
        newrow = choice[0]
        newcol = choice[1]
        validity = True

        if self.gameover():
            self.check_game_over()

        if not self.check_row(newrow) or not self.check_col(newcol):
            raise ValueError
            validity = False


        elif self._board[newrow][newcol] == self._empty and self.check_valid_directions(newrow,newcol, self._turn):
            self.flip_tiles_all_directions(newrow,newcol,self._turn)
            self._board[newrow][newcol] = self._turn
            self._turn = self.switch_turn()
                        

        else:
            raise InvalidMoveError()
            validity = False
        
        return validity


    def check_no_valid_moves_one_player(self, turn:int):
        '''Checks if a player has any available moves'''
        validity = False
        for row in range(self._rows):
            for column in range(self._cols):
                if self._board[row][column] == self._empty:
                    if self.check_valid_directions(row,column,turn):
                        validity = True
        return validity

    def no_valid_moves_one_player(self,turn:int):
        '''Switches turn if a player does not have any available moves'''
        for row in range(self._rows):
            for column in range(self._cols):
                if self._board[row][column] == self._empty:
                    if not self.check_valid_directions(row,column,turn):
                        self._turn = self.switch_turn()
                    
    

    def flip_tiles_one_direction(self, row: int, col: int, rowdelta: int, coldelta: int, turn: int): 
        '''Flips tiles in the specified direction, if possible'''
        nums = []
        for i in range(16):
            if self.check_row(row + rowdelta * i) and self.check_col(col + coldelta * i):
                nums.append(self._board[row + rowdelta * i][col + coldelta * i])
        print(nums)

        try:
            second = nums[1:].index(turn) + 1
            for x in range(1,second):
                if self._empty not in nums[1:second] and nums[1] != turn:
                    self._board[row + rowdelta * x][col + coldelta * x] = turn
        
        except ValueError:
            pass

        

    def check_valid_direction(self, row: int, col: int, rowdelta: int, coldelta: int, turn: int):
        '''Checks if any tiles can be flipped in the specified direction'''
        nums = []
        validity = False
        for i in range(16):
            if self.check_row(row + rowdelta * i) and self.check_col(col + coldelta * i):
                nums.append(self._board[row + rowdelta * i][col + coldelta * i])      
        try:
            second = nums[1:].index(turn) + 1
            for x in range(1,second):
                if self._empty not in nums[1:second] and nums[1] != turn:
                    validity = True
                    
        except ValueError:
            validity = False

        return validity
        
    

    def flip_tiles_all_directions(self, row: int, col: int, turn: int):
        '''Flips tiles in each direction, if possible'''
        directionslist = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        for directions in directionslist:
            self.flip_tiles_one_direction(row, col, directions[0], directions[1], turn)


    def check_valid_directions(self, row: int, col: int, turn: int):
        '''Checks all directions if flipping is possible'''
        directionslist = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
        validitylist = []
        validity = True
        for directions in directionslist:
            validitylist.append(self.check_valid_direction(row, col, directions[0], directions[1], turn))
        if True not in validitylist:
            validity = False
        return validity

        

    def scoreboard(self):
        '''Counts the number of black and white pieces on the current board'''
        bcounter = 0
        wcounter = 0
        for row in self._board:
            for col in row:
                if col == self._black:
                    bcounter += 1
                elif col == self._white:
                    wcounter += 1
        self._blackscore = bcounter
        self._whitescore = wcounter


    def determine_winner(self):
        '''Determines the winner based on how the game was specified to be won'''
        winner = self._empty
        if self._how_to_win == '>':
            if self._blackscore > self._whitescore:
                winner = 'B'
            elif self._blackscore == self._whitescore:
                winner = 'NONE'
            else:
                winner = 'W'

                
        elif self._how_to_win == '<':
            if self._blackscore < self._whitescore:
                winner = 'B'
            elif self._blackscore == self._whitescore:
                winner = 'NONE'
            else:
                winner = 'W'

        
        return winner
        

    def gameover(self):
        '''Returns true if there are no more valid moves for both players'''
        game_over = False
        if not self.check_no_valid_moves_one_player(self._turn) and not self.check_no_valid_moves_one_player(self.switch_turn()):
            game_over = True
        
        return game_over

    def check_game_over(self):
        '''Raises GameOverError if the game is over'''
        if self.determine_winner() != self._empty:
            raise GameOverError()

    def check_row(self, num: int):
        '''Returns true if the given row number is valid and false otherwise'''
        return 0 <= num < self._rows

    
    def check_col(self, num: int):
        '''Returns true if the given column number is valid and false otherwise'''

        return 0 <= num < self._cols
