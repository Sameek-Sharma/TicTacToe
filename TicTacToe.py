import numpy as np

choice_board = np.array([[1,2,3],[4,5,6],[7,8,9]])
board = np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])

turn = 0 

def check_for_win(): #WIN CONDITIONS NOTE FIX
    if board[0,0] == 'X' and board[0,1] == 'X' and board[0,2] == 'X':
        return('PLayer 1 WINS')
    if board[1,0] == 'X' and board[1,1] == 'X' and board[1,2] == 'X':
        return('PLayer 1 WINS')
    if board[2,0] == 'X' and board[2,1] == 'X' and board[2,2] == 'X':
        return('Player 1 WINS')
    if board[0,0] == 'X' and board[1,0] == 'X' and board[2,0] == 'X':
        return('Player 1 WINS')
    if board[0,1] == 'X' and board[1,1] == 'X' and board[2,1] == 'X':
        return('PLayer 1 WINS')
    if board[0,2] == 'X' and board[1,2] == 'X' and board[2,2] == 'X':
        return('PLayer 1 WINS')
    if board[0,0] == 'X' and board[1,1] == 'X' and board[2,2] == 'X':
        return('Player 1 WINS')
    if board[0,2] == 'X' and board[1,1] == 'X' and board[2,0] == 'X':
        return('Player 1 Wins')
    
    if board[0,0] == 'O' and board[0,1] == 'O' and board[0,2] == 'O':
        return('PLayer 2 WINS')
    if board[1,0] == 'O' and board[1,1] == 'O' and board[1,2] == 'O':
        return('PLayer 2 WINS')
    if board[2,0] == 'O' and board[2,1] == 'O' and board[2,2] == 'O':
        return('PLayer 2 WINS')
    if board[0,0] == 'O' and board[1,0] == 'O' and board[2,0] == 'O':
        return('PLayer 2 WINS')
    if board[0,1] == 'O' and board[1,1] == 'O' and board[2,1] == 'O':
        return('PLayer 2 WINS')
    if board[0,2] == 'O' and board[1,2] == 'O' and board[2,2] == 'O':
        return('PLayer 2 WINS')
    if board[0,0] == 'O' and board[1,1] == 'O' and board[2,2] == 'O':
        return('Player 2 WINS')
    if board[0,2] == 'O' and board[1,1] == 'O' and board[2,0] == 'O':
        return('PLayer 2 WINS')
    else:
        return(False)

def turn_tracker(): #should add 1 every complete turn to turn total
    global turn
    turn = turn + 1
    return(turn)

def turn_checker(): #checks for who's move it is
    if turn%2 == 0:
        return(True)
    if turn%2 != 0:
        return(False)

def player_turn(): #asks for input from each player
    playerturn = input('Choose Square: ')
    if playerturn.isdigit():
        print(choice(int(playerturn)))
        turn_tracker()
        next_turn()
    else:
        player_turn()

def find_index(p): #finds where user inputs their turn
    position_vector = np.where(choice_board == p)
    return(position_vector)

def available_moves(): #finds available spaces on board
    global option_board
    option_board = np.where(choice_board == 0 , None , choice_board)
    return(option_board)

def choice(x): #Puts user input onto the game board
    if turn_checker() == True:
        board[find_index(x)[0],find_index(x)[1]] = 'X'
        choice_board[find_index(x)[0],find_index(x)[1]] = 0
        return(print(board))
    else:
        board[find_index(x)[0],find_index(x)[1]]= 'O'
        choice_board[find_index(x)[0],find_index(x)[1]] = 0
        return(print(board)) 

def next_turn(): #Calls functions for game to be played
    if turn_checker() == True:
        if check_for_win() == False:
            print("Player 1's Turn")
            print(available_moves())
            player_turn()
        else:
            print(check_for_win())
            return
    if turn_checker() == False:
        if check_for_win() == False:
            print("Player 2's Turn")
            print(available_moves())
            player_turn()
        else:
            print(check_for_win())
            return
        
def init(): #initializes the game
    print("Player 1's Turn")
    print(available_moves())
    player_turn()

if __name__ == "__main__": #runs file as wanted
    init()