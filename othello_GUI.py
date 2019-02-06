# Sophia Tao, 20293428, stao3@uci.edu

import tkinter
import point
import othello_logic
import spots_model

DEFAULT_FONT = ('Calibri', 10)

#Game Setup; Takes input from user on game conditions
class InputDialog:
    def __init__(self):
        
        self._dialog_window = tkinter.Toplevel()



        #"Please input your preferences" text at top of popup window
        input_label = tkinter.Label(
            master = self._dialog_window, text = 'Please input your preferences',
            font = DEFAULT_FONT)
        input_label.grid(
            row = 0, column = 0, columnspan = 5, padx = 10, pady = 20,
            sticky = tkinter.W)



        #"Number of Rows" text
        row_label = tkinter.Label(
            master = self._dialog_window, text = '# of Rows:',
            font = DEFAULT_FONT)
        row_label.grid(row = 1, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.W)
        #Dropdown menu for rows
        self._row_var = tkinter.IntVar()
        self._row_var.set(4)
        row_options = tkinter.OptionMenu(self._dialog_window, self._row_var,
                                         4, 6, 8, 10, 12, 14, 16)
        row_options.grid(row = 1, column = 1, padx = 10, pady = 10, sticky = tkinter.E)



        #"Number of Columns" text
        col_label = tkinter.Label(
            master = self._dialog_window, text = '# of Columns:',
            font = DEFAULT_FONT)
        col_label.grid(row = 2, column = 0, padx = 10, pady = 10,
                       sticky = tkinter.W)
        #Dropdown menu for columns
        self._col_var = tkinter.IntVar()
        self._col_var.set(4)
        col_options = tkinter.OptionMenu(self._dialog_window, self._col_var,
                                         4, 6, 8, 10, 12, 14, 16)
        col_options.grid(row = 2, column = 1, padx = 10, pady = 10, sticky = tkinter.E)
        


        #"First Player" text
        first_player_label = tkinter.Label(
            master = self._dialog_window, text = 'First Player:',
            font = DEFAULT_FONT)
        first_player_label.grid(row = 3, column = 0, padx = 10, pady = 10,
                                sticky = tkinter.W)
        #Dropdown menu for first player
        self._fp_var = tkinter.StringVar()
        self._fp_var.set('Black')
        first_player_options = tkinter.OptionMenu(self._dialog_window, self._fp_var,
                                         'Black', 'White')
        first_player_options.grid(row = 3, column = 1, padx = 10, pady = 10, sticky = tkinter.E)
        
    

        #"Most or least discs win?" text
        discs_winner_label = tkinter.Label(
            master = self._dialog_window, text = 'Most or least discs win?:',
            font = DEFAULT_FONT)
        discs_winner_label.grid(row = 4, column = 0, padx = 10, pady = 10,
                                sticky = tkinter.W)
        #Dropdown menu for win condition
        self._dw_var = tkinter.StringVar()
        self._dw_var.set('Most')
        winner_options = tkinter.OptionMenu(self._dialog_window, self._dw_var,
                                         'Most', 'Least')
        winner_options.grid(row = 4, column = 1, padx = 10, pady = 10, sticky = tkinter.E)



        #Widget container
        button_frame = tkinter.Frame(master = self._dialog_window)

        button_frame.grid(
            row = 5, column = 0, columnspan = 2, padx = 10, pady = 10,
            sticky = tkinter.E + tkinter.S)

        

        #OK button
        ok_button = tkinter.Button(
            master = button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok_button)

        ok_button.grid(row = 0, column = 0, padx = 10, pady = 10)



        #Cancel button
        cancel_button = tkinter.Button(
            master = button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel_button)

        cancel_button.grid(row = 0, column = 1, padx = 10, pady = 10)


        #Dialog window grid row and column configurations
        self._dialog_window.columnconfigure(0, weight = 1)
        self._dialog_window.columnconfigure(1, weight = 1)

        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(2, weight = 1)
        self._dialog_window.rowconfigure(3, weight = 1)
        self._dialog_window.rowconfigure(4, weight = 1)
        self._dialog_window.rowconfigure(5, weight = 1)

        

        #Check if OK was clicked
        self._ok_clicked = False

        #Initial conditions prior to input
        self._row_choice = 0
        self._col_choice = 0
        self._fp_choice = 0
        self._dw_choice = ''



    def show(self) -> None:
        '''Shows the input dialog'''
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()

    def was_ok_clicked(self) -> bool:
        '''Returns True if the OK button was clicked and False otherwise'''
        return self._ok_clicked

    def get_rows(self) -> int:
        '''Returns the number of rows inputted'''
        return self._row_choice

    def get_columns(self) -> int:
        '''Returns the number of columns inputted'''
        return self._col_choice

    def get_first_player(self) -> str:
        '''Returns the first player inputted'''
        return self._fp_choice

    def get_discs_winner(self) -> str:
        '''Returns if the most or least discs win'''
        return self._dw_choice
        
    def _on_ok_button(self) -> None:
        '''Converts the input to usable values after the OK button was clicked'''
        
        self._ok_clicked = True
        
        self._row_choice = self._row_var.get()
        self._col_choice = self._col_var.get()

        #Converts Black to 1 and White to 2
        if self._fp_var.get() == 'Black':
            self._fp_choice = 1
        else:
            self._fp_choice = 2

        #Converts Most to > and Least to <
        if self._dw_var.get() == 'Most':
            self._dw_choice = '>'
        else:
            self._dw_choice = '<'
        
        #Destroy window after confirmation of conditions
        self._dialog_window.destroy()


    def _on_cancel_button(self) -> None:
        '''Closes the input dialow window if cancel is clicked'''
        self._dialog_window.destroy()
        

class OthelloApplication:
    def __init__(self):
        
        self._root_window = tkinter.Tk()



        #"FULL VERSION" text
        version_label = tkinter.Label(
            master = self._root_window, text = 'FULL VERSION',
            font = ('Calibri', 8))
        version_label.grid(row = 0, column = 0,
                           sticky = tkinter.N + tkinter.E)


        
        #Title
        self._game_text = tkinter.StringVar()
        self._game_text.set('OTHELLO')
        self._game_label = tkinter.Label(
            master = self._root_window, textvariable = self._game_text,
            font = ('Calibri', 24))
        self._game_label.grid(row = 1, column = 0, padx = 10, pady = 10)



        #Background
        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 400, height = 400,
            background = '#9589b5')
        self._canvas.grid(
            row = 2, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)



        #Resizing and clicking binding
        self._canvas.bind('<Configure>', self._on_canvas_resized)
        self._canvas.bind('<Button-1>', self._on_canvas_clicked)



        #"Start New Game" button
        self._buttontext = tkinter.StringVar()
        self._buttontext.set('Start New Game')
        self._new_game_button = tkinter.Button(
            master = self._root_window, textvariable = self._buttontext, font = DEFAULT_FONT,
            command = self._on_new_game)
        self._new_game_button.grid(
            row = 3, column = 0, padx = 10, pady = 10)



        #Row and column configuration
        self._root_window.columnconfigure(0, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)



        #Initial conditions prior to input
        self._rows = 0
        self._cols = 0
        self._fp_choice = 0
        self._dw_choice = ''
        self._board = []
        self._spotsboard = [] #Pieces placed on board



        #
        self._spots_b = []
        self._spots_w = []

        self._gamestate = None

        self._input_stage = False
        self._input_stage_turn = 0

    def run(self) -> None:
        '''Runs the graphical user interface'''
        self._root_window.mainloop()
    

    def _on_new_game(self) -> None:
        '''Creates the board and allows the first player to put initial pieces upon clicking the start new game button'''
        dialog = InputDialog()
        dialog.show()

        if dialog.was_ok_clicked():
            self._input_stage = True
            self._rows = dialog.get_rows()
            self._cols = dialog.get_columns()
            self._fp_choice = dialog.get_first_player()
            self._input_stage_turn = self._fp_choice
            self._dw_choice = dialog.get_discs_winner()
            
            self._draw_lines()

            if self._fp_choice == 1:
                self._game_text.set('Black is placing pieces')
            elif self._fp_choice == 2:
                self._game_text.set('White is placing pieces')


            self._new_game_button.destroy()
            self.new_board()
            self.spots_board()
            
            self._next_button = tkinter.Button(
                master = self._root_window, text = 'Next', font = DEFAULT_FONT,
                command = self._on_next)
            self._next_button.grid(
                row = 3, column = 0, padx = 10, pady = 10)

    def _on_next(self) -> None:
        '''Allows the second player to put initial pieces upon clicking the next button'''
        if self._fp_choice == 1:
            self._game_text.set('White is placing pieces')
        elif self._fp_choice == 2:
            self._game_text.set('Black is placing pieces')

        if self._input_stage_turn == 1:
            self._input_stage_turn = 2
        elif self._input_stage_turn == 2:
            self._input_stage_turn = 1
        self._next_button.destroy()
        
        self._proceed_button = tkinter.Button(
            master = self._root_window, text = 'Proceed', font = DEFAULT_FONT,
            command = self._on_proceed)
        self._proceed_button.grid(
            row = 3, column = 0, padx = 10, pady = 10)


    def _on_proceed(self) -> None:
        '''Starts the game upon clicking the proceed button'''
        self._proceed_button.destroy()

        self._input_stage = False
        self._input_stage_turn = 0
        self._gamestate = othello_logic.GameState(self._rows, self._cols, self._fp_choice, self._dw_choice, self._board)
        self._gamestate.scoreboard()
        
        self._score = tkinter.StringVar()
        self._score.set('Black: ' + str(self._gamestate._blackscore) + '    White: ' + str(self._gamestate._whitescore))
        self._scoreboard = tkinter.Label(
            master = self._root_window, textvariable = self._score,
            font = ('Calibri', 20))
        self._scoreboard.grid(row = 3, column = 0, padx = 10, pady = 10)

        if self._gamestate.gameover():
            if self._gamestate.determine_winner() == 'B': 
                self._game_text.set("WINNER: BLACK")
            elif self._gamestate.determine_winner() == 'W': 
                self._game_text.set("WINNER: WHITE")
            elif self._gamestate.determine_winner() == 'NONE': 
                self._game_text.set("NO WINNER")
        else:
            if self._gamestate.get_turn() == 1:
                self._game_text.set("Black's turn")
            elif self._gamestate.get_turn() == 2:
                self._game_text.set("White's turn")

            
            

    def _draw_lines(self) -> None:
        '''Draws the lines on the board based on the specified number of rows and columns'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        
        for r in range(1,self._rows):
            self._canvas.create_line(
                canvas_width * (1/self._rows) * r, 0,
                canvas_width * (1/self._rows) * r, canvas_height,
                fill = 'white')
            
        for c in range(1,self._cols):
            self._canvas.create_line(
                0, canvas_height * (1/self._cols) * c,
                canvas_width, canvas_height * (1/self._cols) * c,
                fill = 'white')


    def top_left(self) -> list:
        '''Returns a list of the top left coordinates of each grid square'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        topleftlist = []
        for c in range(self._cols):
            for r in range(self._rows):
                topleft_x = canvas_width * (1/self._rows) * r
                topleft_y = canvas_height * (1/self._cols) * c
                topleftlist.append([topleft_x,topleft_y])
        return topleftlist

    def bottom_right(self) -> list:
        '''Returns a list of the bottom right coordinates of each grid square'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        bottomrightlist = []
        for c in range(1, self._cols+1):
            for r in range(1, self._rows+1):
                bottomright_x = canvas_width * (1/self._rows) * r
                bottomright_y = canvas_height * (1/self._cols) * c
                bottomrightlist.append([bottomright_x,bottomright_y])
        return bottomrightlist

    def paired_coordinates(self):
        '''Returns a list of the pairs of top left and bottom right coordinates'''
        pairlist = []
        for i in range(len(self.top_left())):
            pairlist.append([self.top_left()[i],self.bottom_right()[i]])
        return pairlist
    
    def point_list(self):
        '''Returns a list of top left and bottom right points'''
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()
        pointlist = []
        for pc in self.paired_coordinates():
            tl = point.from_pixel(pc[0][0],pc[0][1],canvas_width, canvas_height)
            br = point.from_pixel(pc[1][0],pc[1][1],canvas_width, canvas_height)
            pointlist.append([tl,br])
        return pointlist
    
    def potential_spots(self):
        '''Returns a list of all the potential spots on the board'''
        potentialspots = []
        for p in self.point_list():
            potentialspots.append(spots_model.Spot(p[0],p[1]))
        return potentialspots


    def spots_board(self):
        '''Creates a multidimensional array to represent all the potential spots on the board'''
        spotsboard = []
        for i in range(self._rows):
            spotsboard.append(self.potential_spots()[i*self._cols:(i+1)*self._cols])
        self._spotsboard = spotsboard            

    def new_board(self):
        '''Creates a new board'''
        board = []
        for r in range(self._rows):
            board.append([])
            for c in range(self._cols):
                board[-1].append(0)
        
        self._board = board
            


    def handle_click(self, clickpoint:point.Point):
        '''Handles the event in which a click is registered on the board'''
        for r in range(self._rows):
            for c in range(self._cols):
                if self._spotsboard[r][c].contains(clickpoint):
                    if self._input_stage and self._input_stage_turn == 1:
                        if self._spotsboard[r][c] not in self._spots_b:
                            self._spots_b.append(self._spotsboard[r][c])
                            self._board[r][c] = self._input_stage_turn
                        else:
                            ind = self._spots_b.index(self._spotsboard[r][c])
                            del self._spots_b[ind]
                            self._board[r][c] = 0

                    elif self._gamestate != None and self._gamestate.get_turn() == 1:
                        self._gamestate.move([r,c])
                        if self._spotsboard[r][c] not in self._spots_b:
                            self._spots_b.append(self._spotsboard[r][c])
                        
                    elif self._input_stage and self._input_stage_turn == 2:
                        if self._spotsboard[r][c] not in self._spots_w:
                            self._spots_w.append(self._spotsboard[r][c])
                            self._board[r][c] = self._input_stage_turn
                        else:
                            ind = self._spots_w.index(self._spotsboard[r][c])
                            del self._spots_w[ind]
                            self._board[r][c] = 0
                    elif self._gamestate != None and self._gamestate.get_turn() == 2:
                        self._gamestate.move([r,c])
                        if self._spotsboard[r][c] not in self._spots_w:
                            self._spots_w.append(self._spotsboard[r][c])
        
    
    def _on_canvas_resized(self, event: tkinter.Event) -> None:
        '''Resizes the game'''
        self._redraw()

    def _on_canvas_clicked(self, event: tkinter.Event) -> None:
        '''Handles clicks and redraws the canvas'''
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_point = point.from_pixel(
            event.x, event.y, width, height)

        self.handle_click(click_point)
        

        
        if self._gamestate != None:
            self._gamestate.scoreboard()
            self._score.set('Black: ' + str(self._gamestate._blackscore) + '    White: ' + str(self._gamestate._whitescore))
            if not self._gamestate.check_no_valid_moves_one_player(self._gamestate.get_turn()):
                self._gamestate.no_valid_moves_one_player(self._gamestate.get_turn())

            if self._gamestate.gameover():
                if self._gamestate.determine_winner() == 'B': 
                    self._game_text.set("WINNER: BLACK")
                elif self._gamestate.determine_winner() == 'W': 
                    self._game_text.set("WINNER: WHITE")
                elif self._gamestate.determine_winner() == 'NONE': 
                    self._game_text.set("NO WINNER")
            
            else:
                if self._gamestate.get_turn() == 1:
                    self._game_text.set("Black's turn")
                elif self._gamestate.get_turn() == 2:
                    self._game_text.set("White's turn")
                    
        self._redraw()


    def _redraw(self):
        '''Redraws the board and spots'''
        self._canvas.delete(tkinter.ALL)
                
        canvas_width = self._canvas.winfo_width()
        canvas_height = self._canvas.winfo_height()

        self._draw_lines()
        
   
        if self._gamestate != None:
            for r in range(self._rows):
                for c in range(self._cols):
                    if self._board[r][c] == 1:
                        if self._spotsboard[r][c] not in self._spots_b:
                            self._spots_b.append(self._spotsboard[r][c])
                    if self._board[r][c] == 2:
                        if self._spotsboard[r][c] not in self._spots_w:
                            self._spots_w.append(self._spotsboard[r][c])
            if self._gamestate.get_turn() == 2:
                for bs in self._spots_b:
                    if bs in self._spots_w:
                        self._spots_w.remove(bs)
            elif self._gamestate.get_turn() == 1:
                for ws in self._spots_w:
                    if ws in self._spots_b:
                        self._spots_b.remove(ws)

        
        for bs in self._spots_b:
            topleftb = bs._top_left.pixel(canvas_width, canvas_height)
            bottomrightb = bs._bottom_right.pixel(canvas_width, canvas_height)
            self._canvas.create_oval(topleftb[0], topleftb[1],
                                     bottomrightb[0], bottomrightb[1],
                                     fill = 'black', outline = 'white')
        for ws in self._spots_w:
            topleftw = ws._top_left.pixel(canvas_width, canvas_height)
            bottomrightw = ws._bottom_right.pixel(canvas_width, canvas_height)
            self._canvas.create_oval(topleftw[0], topleftw[1],
                                     bottomrightw[0], bottomrightw[1],
                                     fill = 'white', outline = 'black')
        
 
        

        

if __name__ == '__main__':
    OthelloApplication().run()
