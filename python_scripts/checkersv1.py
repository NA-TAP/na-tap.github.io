#Checkers
def create_new_board():
    return [['b', '.', 'b', '.', 'b', '.', 'b', '.'],
             ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
             ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', 'r', '.', 'r', '.', 'r', '.', 'r'],
             ['r', '.', 'r', '.', 'r', '.', 'r', '.'],
             ['.', 'r', '.', 'r', '.', 'r', '.', 'r']]
def print_board(board):
    print('  0 1 2 3 4 5 6 7')
    for i in range(8):
        print(i, end=' ')
        for j in range(8):
            print(board[i][j], end=' ')
        print()
def is_valid_move(board, player, start_row, start_col, end_row, end_col):
    if board[start_row][start_col] == '.':
        return False
    if board[end_row][end_col] != '.':
        return False
    if player == 'r':
        if start_row >= end_row:
            return False
    if player == 'b':
        if start_row <= end_row:
            return False
    if abs(start_row - end_row) != abs(start_col - end_col):
        return False
    if abs(start_row - end_row) > 2:
        return False
    if abs(start_row - end_row) == 2:
        if board[(start_row + end_row) // 2][(start_col + end_col) // 2] == '.':
            return False
        if board[(start_row + end_row) // 2][(start_col + end_col) // 2].lower() == player:
            return False
    return True
def make_move(board, player, start_row, start_col, end_row, end_col):
    if is_valid_move:
        board[end_row][end_col] = board[start_row][start_col]
        board[start_row][start_col] = '.'
def main():
    board = create_new_board()
    player = 'r'
    while True:
        print_board(board)
        print('Player', player)
        start_row = int(input('Enter start row: '))
        start_col = int(input('Enter start col: '))
        end_row = int(input('Enter end row: '))
        end_col = int(input('Enter end col: '))
        if is_valid_move(board, player, start_row, start_col, end_row, end_col):
            make_move(board, player, start_row, start_col, end_row, end_col)
            if player == 'r':
                player = 'b'
            else:
                player = 'r'
        else:
            print('Invalid move')
if __name__ == '__main__':
    main()

#fuck you chatgpt

