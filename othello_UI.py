# Sophia Tao, 20293428, stao3@uci.edu

import othello_logic

print('FULL')

def rows_columns() -> int:
    '''Allows the user to specify the dimensions of the board'''
    
    num = int(input())
    
    return num


def first_player() -> int:
    '''Allows the user to specify which player goes first'''
    
    fp = input().upper()
    
    if fp == 'B':
        num = 1
        
    elif fp == 'W':
        num = 2
        
    return num


def how2win() -> str:
    '''Allows the user to specify how the game is won'''
    moreless = input()

    return moreless


def initial_board(rows: int, cols: int) -> [list]:
    '''Allows the user to input a starting board'''
    board = []
    counter = 0
    while len(board) < rows:
        row = input().upper().split()
        if len(row) == cols:
            for col in range(len(row)):
                if row[col] in '.BW':
                    counter += 1
                    if row[col] == 'B':
                        row[col] = 1
                    elif row[col] == 'W':
                        row[col] = 2
                    elif row[col] == '.':
                        row[col] = 0
            if counter == cols:
                board.append(row)
                counter = 0
            
    else:
        return board
    

def print_board(game_state:othello_logic.GameState, rows: int, cols: int):
    '''Prints the board'''
    for row in range(rows):
        for column in range(cols):
            if game_state._board[row][column] == 0:
                print('.', end = ' ')
            elif game_state._board[row][column] == 1:
                print('B', end = ' ')
            elif game_state._board[row][column] == 2:
                print('W', end = ' ')
        print()
    

def specify_move(row: int, col: int) -> list:
    '''Allows the user to specify a cell to put their piece in'''
    move_list = []
    move = input().split()
    
    for num in move:
        move_list.append(int(num))
    return move_list

def valid_invalid_move(game_state:othello_logic.GameState, row: int, col: int):
    '''Determines whether a move is valid or invalid'''
    while True:
        try:
            choice = specify_move(row, col)
            if game_state.move(choice):
                print('VALID')
                return
        except:
            print('INVALID')


def turn(game_state: othello_logic.GameState):
    '''Prints the current player's turn'''
    if game_state._turn == 1:
        print('TURN: B')
    elif game_state._turn == 2:
        print('TURN: W')
            
def run_program():
    '''Runs the program'''
    rows = rows_columns()
    columns = rows_columns()
    firstplayer = first_player()
    moreless = how2win()
    initialboard = initial_board(rows, columns)
    game_state = othello_logic.GameState(rows, columns, firstplayer, moreless, initialboard)
    while True:
        if not game_state.check_no_valid_moves_one_player(game_state._turn):
            game_state.no_valid_moves_one_player(game_state._turn)
        game_state.scoreboard()
        print('B: {}  W: {}'.format(game_state._blackscore, game_state._whitescore))
        print_board(game_state, rows, columns)
        if game_state.gameover():
            print('WINNER: {}'.format(game_state.determine_winner()))
            break
        else:
            turn(game_state)
            decision = valid_invalid_move(game_state, rows, columns)
        
if __name__ == '__main__':
    run_program()
