# A simple program which pretends to play tic-tac-toe with the user
# The first move belongs to the computer − it always puts its first 'X' in the middle of the board.
# The user inputs their move by entering the number of the square they choose − the number must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied.

from random import randrange

number_to_coords = {"1": (0,0), "2": (0,1), "3": (0,2), "4": (1,0), "5": (1,1), "6": (1,2), "7": (2,0), "8": (2,1), "9":(2,2)}

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    row_base = "-------+"*3
    for row in range(3):
        print("+", row_base, sep="")
        for cell_row in range(3):
            if cell_row != 1:
                for column in range(3):
                    print("|       ", end="")
                print("|")
            else:
                for column in range(3):    
                    print(f"|   {board[row][column]}   ", end="")
                print("|")
    print("+", row_base, sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        users_move = input("Please enter the number of the square you choose: ")
        if users_move not in number_to_coords:
            print("The number must be an integer, be greater than 0 and less than 10, and it cannot point to a field which is already occupied.")
            continue
        user_coords = number_to_coords[users_move]
        if user_coords in make_list_of_free_fields(board):
            row, column = user_coords
            board[row][column] = "O"
            display_board(board)
            break
        else:
            print("The field is already occupied.")
            continue
        

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields_list = [(1, 1)] # because this field is occupied with "X" by default
    for row in range(3):
        for column in range(3):
            if str(board[row][column]).isnumeric():
                free_field = row, column
                free_fields_list.append(free_field)
    return free_fields_list

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # Check if a horizontal line win
    for row in board:
        count = 0
        for element in row:
            if element == sign:
                count += 1
            if count == 3:
                return True
    # Check if vertical line win
    for column in range(3):
        if sign == board[0][column] == board[1][column] == board[2][column]:
            return True
    # Check if diagonal line win
    if sign == board[0][0] == board[1][1] == board[2][2] or sign == board[0][2] == board[1][1] == board[2][0]:
        return True
    return False      
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    comp_move = str(randrange(1, 10))   
    row, column = number_to_coords[comp_move]
    while not (row, column) in make_list_of_free_fields(board):
        comp_move = str(randrange(1, 10))
        row, column = number_to_coords[comp_move]
    board[row][column] = "X"
    display_board(board)

def is_game_over():
    if victory_for(board, "O"):
        print("You won!")
        return True
    elif victory_for(board, "X"):
        print("Computer won!")
        return True
    elif len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        return True
    return False

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

display_board(board)
game_over = False
while not game_over:
    enter_move(board)
    if is_game_over():
        break
    draw_move(board)
    game_over = is_game_over()

