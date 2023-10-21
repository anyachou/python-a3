""" A fancy tic-tac-toe game for CSSE1001/7030 A1. """
from constants import *

Board = list[list[str]]
Pieces = list[int]
Move = tuple[int, int, int] 

# Write your functions here

# 4.1 num hours() -> float    
def num_hours() ->float : 
    return 65

# 4.2 generate initial pieces(num pieces: int) -> Pieces
def generate_initial_pieces(num_pieces):
    arr = []
    for i in range(1, num_pieces + 1): 
        arr.append(i)
    return arr
# ------------------------------------------------------------------------------------------------------------------------------
# 4.3 initial state() -> Board
def initial_state():
    arr = []
    for i in range(GRID_SIZE):
        inner_arr = []
        for j in range(GRID_SIZE):
            inner_arr.append(EMPTY)
        arr.append(inner_arr)
    return arr
# ------------------------------------------------------------------------------------------------------------------------------
# 4.4 place piece(board: Board, player: str, pieces available: Pieces, move: Move ) -> None
def place_piece(board, player, pieces, move):
    pieces.remove(move[2]) #（1,2,3)
    board[move[0]][move[1]] = player + str(move[2]) #O3 「
# ------------------------------------------------------------------------------------------------------------------------------
# 4.5 print game(board: Board, naught pieces: Pieces, cross pieces: Pieces) -> None
def print_game(board, naught_pieces, cross_pieces) -> None:
    print(NAUGHT + " has: " + ", ".join(map(str, naught_pieces)))
    print(CROSS + " has: " + ", ".join(map(str, cross_pieces)))
    print("")

    # Print column numbers
    col_numbers = "   " + "  ".join(str(i + 1) for i in range(len(board)))
    print(col_numbers)

    # Print horizontal line
    print(f"  {'-' * 3 * len(board)}")

    # Print rows
    for row_idx, row in enumerate(board):
        print(f"{row_idx + 1}|", end="")
        for col_idx, cell in enumerate(row):
            if cell == EMPTY:
                print("  |", end="")
            else:
                player = cell[0]
                piece_number = cell[1]
                print(f"{player}{piece_number}|", end="")
        print("\n  " + f"{'-' * 3 * len(board)}")
# ------------------------------------------------------------------------------------------------------------------------------
# 4.6 process move(move: str) -> Move | None
def process_move(move: str) -> Move or None:
    move_arr = move.split()
    if len(move_arr) == 3 and all(str(item).isdigit() for item in move_arr) and all(int(item) > 0 for item in move_arr) and int(move_arr[0]) <= GRID_SIZE and int(move_arr[1]) <= GRID_SIZE:
        # print(f"({int(move_arr[0])-1}, {int(move_arr[1])-1}, {move_arr[2]})")
        return (int(move_arr[0])-1, int(move_arr[1])-1, int(move_arr[2]))
    
    if len(move_arr) != 3 or any(len(str(item)) != 1 for item in move_arr):
        print(INVALID_FORMAT_MESSAGE)
        return
    
    for i in range(3):
        error=""
        if i == 0:
            error=INVALID_ROW_MESSAGE
        elif i == 1:
            error=INVALID_COLUMN_MESSAGE
        elif i == 2:
            error=INVALID_SIZE_MESSAGE

        if str(move_arr[i]).isalpha() or int(move_arr[i]) <= 0:
            print(error)
            return
        
        if (i == 0 or i == 1) and int(move_arr[i]) > GRID_SIZE:
            print(error)
            return
# ------------------------------------------------------------------------------------------------------------------------------        
# 4.7 get player move() -> Move
# def get_player_move():
#     while True:
#         arr=input('Enter your move: ').split()
#         if arr[0].lower() == "h":
#             print(HELP_MESSAGE)
#             continue
        
#         if len(arr) != 3:
#             print(INVALID_FORMAT_MESSAGE)
#             continue
        
#         try:
#             row, col, size = map(int, arr)
#         except ValueError:
#             print(INVALID_FORMAT_MESSAGE)
#             continue
        
#         if row < 1 or col < 1:
#             print(INVALID_ROW_MESSAGE)
#             continue
        
#         if size < 1 or size > GRID_SIZE ** 2:
#             print(INVALID_SIZE_MESSAGE)
#             continue
        
#         row -= 1
#         col -= 1
#         return row, col, size

def get_player_move():
    result=process_move(input('Enter your move: '))
    return result if result is not None else get_player_move()
        
# --------------------------------------------------------------------------------------------------------
# 4.8 check move(board: Board, pieces available: Pieces, move: Move) -> bool
def check_move(board, pieces: Pieces, move) -> bool:
    row, col, piece = move
    # if all(int(item) != piece for item in pieces):
    #     print(INVALID_MOVE_MESSAGE)
    #     return False

    if (board[row][col] == EMPTY or int(board[row][col][1]) < piece) and any(int(item) == piece for item in pieces):
        return True

    print(INVALID_MOVE_MESSAGE)
    return False

# --------------------------------------------------------------------------------------------------------
# 4.9 check win(board: Board) -> str | None
def check_win(board):
    element = EMPTY
    left_cross_arr = []
    right_cross_arr = []
    for i in range(GRID_SIZE):
        element = board[i][i]
        if element == EMPTY:
            continue
        element = element[0]
        # row
        if all(item.startswith(element) for item in board[i]):
            return element
        # column
        col_arr = []
        for j in range(GRID_SIZE):
            col_arr.append(board[j][i][0])
        if len(set(col_arr)) == 1:
            return element
        # cross element
        left_cross_arr.append(element)
        right_cross_arr.append(board[i][GRID_SIZE - 1 - i][0])
    cross_win = (len(left_cross_arr) == GRID_SIZE and len(set(left_cross_arr)) == 1) or (len(right_cross_arr) == GRID_SIZE and len(set(right_cross_arr)) == 1 )
    if element != EMPTY and cross_win:
        print(9)
        return element
# ---------------------------------------------------------------------------------------------------------------------
# 4.10 check stalemate(board: Board, naught pieces: Pieces, cross pieces: Pieces) -> bool
def check_stalemate(board, naught_pieces, cross_pieces):
    naught_max = max(naught_pieces)
    cross_max = max(cross_pieces)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == EMPTY:
                return False
            symbol = board[i][j][0]
            value = int(board[i][j][1])
            if (symbol == NAUGHT and value < naught_max ) or (symbol == CROSS and value < cross_max):
                return False
    return True
# ---------------------------------------------------------------------------------------------------------------------
# 4.11 main() -> None
def main() -> None:
    again="y"
    while again.lower() == "y":
        again=""
        board = initial_state()
        x_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
        o_pieces = generate_initial_pieces(PIECES_PER_PLAYER)
        player=NAUGHT
        is_due=False

        while None == check_win(board) and not check_stalemate(board, o_pieces, x_pieces):
            
            print_game(board, o_pieces, x_pieces)
            print("")
            print(f"{str(player)} turn to move")
            print("")
            move = get_player_move()
            pieces = o_pieces if player == NAUGHT else x_pieces
            if check_move(board, pieces, move):
                place_piece(board, player, pieces, move)
            
            if check_stalemate(board, o_pieces, x_pieces):
                if None != check_win(board):
                    break
                else:
                    is_due=True

            if player == NAUGHT:
                player = CROSS
            elif player == CROSS:
                player = NAUGHT
        
        if player == NAUGHT:
            player = CROSS
        elif player == CROSS:
            player = NAUGHT
        print_game(board, o_pieces, x_pieces)

        if is_due:
            print("due")
        else:
            print(f"{player} wins!")
        again = input("Play again? ")

        # print("due. ")
        # break
        # if "Y" != input("Play Game Again? (Y/N)"):
        #     break        

# ---------------------------------------------------------------------------------------------------------------------------
# def main() -> None:
#     num_hours()
#     O = generate_initial_pieces(PIECES_PER_PLAYER)
#     X = generate_initial_pieces(PIECES_PER_PLAYER)
#     b = initial_state()
#     place_piece(b, NAUGHT, O, (1, 1, 1))
#     place_piece(b, CROSS, X, (0, 0, 1))
#     print_game(b, O, X)
#     process_move("1 1 1")
#     get_player_move()
#     check_move(b,O,(1,1,5))
#     check_win(b)
#     pass

# ------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()


