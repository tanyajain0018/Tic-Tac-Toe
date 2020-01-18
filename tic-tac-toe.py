# CS-UY 1114
# Final project

import turtle
import time
import random
import ctypes

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def draw_board(board):
    """
    signature: list(str) -> NoneType
    Given the current state of the game, draws
    the board on the screen, including the
    lines and the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.clear()
    # code below draws the board
    turtle.up()
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.down()
    j = 6
    while j >= -6:    #draws the rows and columns for the board
        turtle.up()
        turtle.goto((-turtle.window_width()/2),(turtle.window_height()/j))
        turtle.down()
        turtle.forward(turtle.window_width())
        turtle.up()
        turtle.setheading(-90)
        turtle.goto((-turtle.window_width()/j),(turtle.window_height()/2))
        turtle.down()
        turtle.forward(turtle.window_height())
        turtle.setheading(0)
        j -= 12

            
# code below draws the pieces
# even though both x and zero start at the same position I wrote
# them seperately so I don't have to reset the starting positions every time 
    startingx_for_X = -turtle.window_width()/3
    startingy_for_X = turtle.window_height()/2
    startingx_for_O = -turtle.window_width()/3     
    startingy_for_O = turtle.window_height()/2
    for item in range(9):      #goes through the board list and if sees an "X" draws the x and if sees an "O" draws an O
        if the_board[item] == "X":       #draws the X here
            turtle.up()
            turtle.goto(startingx_for_X,startingy_for_X)
            turtle.setheading(180)
            turtle.forward(turtle.window_width()/6)
            turtle.left(140)
            turtle.down()
            turtle.forward(((turtle.window_height()/3)**(2)+(turtle.window_width()/3)**(2))**(1/2))  #represents the length of the diagonal because the boxes can be rectangle depending on user's screen
            turtle.up()
            turtle.right(140)
            turtle.forward(turtle.window_width()/3)
            turtle.right(140)
            turtle.down()
            turtle.forward(((turtle.window_height()/3)**(2)+(turtle.window_width()/3)**(2))**(1/2))
            turtle.up()
            turtle.goto(0,0)
            turtle.down()
        startingx_for_X += turtle.window_width()/3
        if (item+1)%3 == 0: # if new row brings back x coordinate to the left and moves y coordinate down
            startingx_for_X = -turtle.window_width()/3
            startingy_for_X -= turtle.window_height()/3
        turtle.up()
        if the_board[item] == "O":    #draws the O here
            turtle.goto(startingx_for_O,startingy_for_O)
            turtle.setheading(180)
            turtle.down()
            turtle.circle(turtle.window_height()/6)
        startingx_for_O += turtle.window_width()/3
        if (item+1)%3==0: # if new row brings back x coordinate to the left and moves y coordinate down
            startingy_for_O -= turtle.window_height()/3
            startingx_for_O = -turtle.window_width()/3
    turtle.update()
    
def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    Given a list representing the state of the board
    and an x,y screen coordinate pair indicating where
    the user clicked, update the board
    with an O in the corresponding position. Your
    code will need to translate the screen coordinate
    (a pixel position where the user clicked) into the
    corresponding board position (a value between 0 and
    8 inclusive, identifying one of the 9 board positions).
    The function returns a bool indicated if
    the operation was successful: if the user
    clicks on a position that is already occupied
    or outside of the board area, the move is
    invalid, and the function should return False,
    otherise True.
    """

    if x < -(turtle.window_width()/6):        
        if y > (turtle.window_height()/6):
            if the_board[0] == "_":
                the_board[0] = "O"     # board position 0
                return True
            else:                      #if position already occupied returns false
                return False
        elif y < -(turtle.window_height()/6):
            if the_board[6] == "_":     
                the_board[6] = "O"    # board position 6
                return True
            else:                      #if position already occupied returns false
                return False
        else:
            if the_board[3] == "_":
                the_board[3] = "O"     # board position 3
                return True
            else:                      #if position already occupied returns false
                return False
    elif x > (turtle.window_width()/6):
        if y > (turtle.window_height()/6):
            if the_board[2] == "_":
                the_board[2] = "O"     # board position 2
                return True
            else:                      #if position already occupied returns false
                return False
        elif y < -(turtle.window_height()/6):
            if the_board[8] == "_":
                the_board[8] = "O"     # board position 8
                return True
            else:                      #if position already occupied returns false
                return False
        else:
            if the_board[5] == "_":
                the_board[5] = "O"     # board position 5
                return True
            else:                      #if position already occupied returns false
                return False
    elif x > -(turtle.window_width()/6) and x < (turtle.window_width()/6) :
        if y > (turtle.window_height()/6):
            if the_board[1] == "_":
                the_board[1] = "O"     # board position 1
                return True
            else:                      #if position already occupied returns false
                return False
        elif y < -(turtle.window_height()/6):
            if the_board[7] == "_":
                the_board[7] = "O"     # board position 7
                return True
            else:                      #if position already occupied returns false
                return False
        else:
            if the_board[4] == "_":
                the_board[4] = "O"     # board position 4
                return True
            else:                      #if position already occupied returns false
                return False
    else:                          # if the position outside board it returns false 
        return False
    
def check_for_match(item1, item2, item3, char):   #returns true if the three items have the same character on the board
    """
    signature: int, int, int ,str -> bool
    Returns true if the character specified appears
    three times in the board spaces listed in all_combinations_check
    """
    if the_board[item1] == char and the_board[item2] == char and the_board[item3] == char:
        return True
def all_combinations_check(char):
    """
    signature: str -> bool
    Takes in a character, in this case, the "x" and "O"
    It tests the character for all the combinations
    needed to win the game.
    If the character returns true for that combination,
    then the character wins. 
    """
    if check_for_match(0, 1, 2, char):
        return True
    if check_for_match(3, 4, 5, char):
        return True
    if check_for_match(6, 7, 8, char):
        return True
    if check_for_match(0, 4, 8, char):
        return True
    if check_for_match(6, 3, 0, char):
        return True
    if check_for_match(2, 5, 8, char):
        return True
    if check_for_match(1, 4, 7, char):
        return True
    if check_for_match(2, 4, 6, char):
        return True
    
def check_game_over(board):
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """

    game_over = False
    while game_over == False:
        if all_combinations_check("X") == True:
            turtle.goto(0,0)
            turtle.write("The computer is the Winner!", True, align= "center", font = ("Arial", 15, "bold"))
            game_over = True
            for i in range(9):
                board[i] = "_"
        elif all_combinations_check("O") == True:
            turtle.goto(0,0)
            turtle.write("You win!", True, align= "center", font = ("Arial", 15, "bold"))
            game_over = True
            for i in range(9):
                board[i] = "_"
        elif "_" not in board:
            turtle.goto(0,0)
            turtle.write("No winner", True, align= "center", font = ("Arial", 15, "bold")) 
            game_over = True
            for i in range(9):
                board[i] = "_"
        else:
            game_over = False
        return game_over

def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    opponent = random.randint(0,8)  #creates random number position from 0-8 for computer to occupy
    # code below programs the X to randomly occupy a space, attempt to win if it can, and stop the human player from winning
    if ((board[0] == "X" and board[8] == "X") or (board[2] == "X" and board[6] == "X") or (board[1] == "X" and board[7] == "X") or (board[3] == "X" and board[5] == "X")) and board[4] != "O":
        board[4] = "X"

    elif ((board[1] == "X" and board[2] == "X") or (board[3] == "X" and board[6] == "X") or (board[4] == "X" and board[8] == "X")) and board[0] != "O":
        board[0] = "X"

    elif ((board[0] == "X" and board[1] == "X") or (board[4] == "X" and board[6] == "X") or (board[5] == "X" and board[8] == "X")) and board[2] != "O":
        board[2] = "X"

    elif ((board[0] == "X" and board[3] == "X") or (board[4] == "X" and board[2] == "X") or (board[7] == "X" and board[8] == "X")) and board[6] != "O":
        board[6] = "X"

    elif ((board[6] == "X" and board[7] == "X") or (board[0] == "X" and board[4] == "X") or (board[2] == "X" and board[5] == "X")) and board[8] != "O":
        board[8] = "X"

    elif ((board[0] == "X" and board[2] == "X") or (board[4] == "X" and board[7] == "X")) and board[1] != "O":
        board[1] = "X"

    elif ((board[0] == "X" and board[6] == "X") or (board[4] == "X" and board[5] == "X")) and board[3] != "O":
        board[3] = "X"

    elif ((board[3] == "X" and board[4] == "X") or (board[2] == "X" and board[8] == "X")) and board[5] != "O":
        board[5] = "X"

    elif ((board[1] == "X" and board[4] == "X") or (board[6] == "X" and board[8] == "X")) and board[7] != "O":
        board[7] = "X"

    elif ((board[0] == "O" and board[8] == "O") or (board[2] == "O" and board[6] == "O") or (board[1] == "O" and board[7] == "O") or (board[3] == "O" and board[5] == "O")) and board[4] != "X":
        board[4] = "X"

    elif ((board[1] == "O" and board[2] == "O") or (board[3] == "O" and board[6] == "O") or (board[4] == "O" and board[8] == "O")) and board[0] != "X":
        board[0] = "X"

    elif ((board[0] == "O" and board[1] == "O") or (board[4] == "O" and board[6] == "O") or (board[5] == "O" and board[8] == "O")) and board[2] != "X":
        board[2] = "X"

    elif ((board[0] == "O" and board[3] == "O") or (board[4] == "O" and board[2] == "O") or (board[7] == "O" and board[8] == "O")) and board[6] != "X":
        board[6] = "X"

    elif ((board[6] == "O" and board[7] == "O") or (board[0] == "O" and board[4] == "O") or (board[2] == "O" and board[5] == "O")) and board[8] != "X":
        board[8] = "X"

    elif ((board[0] == "O" and board[2] == "O") or (board[4] == "O" and board[7] == "O")) and board[1] != "X":
        board[1] = "X"

    elif ((board[3] == "O" and board[4] == "O") or (board[2] == "O" and board[8] == "O")) and board[5] != "X":
        board[5] = "X"

    elif ((board[0] == "O" and board[6] == "O") or (board[4] == "O" and board[5] == "O")) and board[3] != "X":
        board[3] = "X"

    elif ((board[1] == "O" and board[4] == "O") or (board[6] == "O" and board[8] == "O")) and board[7] != "X":
        board[7] = "X"
    elif (the_board[opponent] == "_"):
        board[opponent] = "X"
    else :
        do_computer_move(board)
        
def clickhandler(x, y):
    """
    signature: int, int -> NoneType
    This function is called by turtle in response
    to a user click. The parameters are the screen
    coordinates indicating where the click happened.
    The function will call other functions. You do not
    need to modify this function, but you do need
    to understand it.
    """
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if not check_game_over(the_board):
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board) 
    turtle.mainloop()

main()
