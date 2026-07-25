# Tic Tac Toe
import random

print('Welcome to tic-tac-toe!')
print('the spaces are as so:\n7|8|9\n-+-+-\n4|5|6\n-+-+-\n1|2|3')
def who_goes_first():
    if random.randint(0, 1) == 1:
        return ['X', 'O']
    else:
        return ['O', 'X']

first_person = who_goes_first()
print('You are ' + first_person[0])

def draw_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def make_new_board():
    return [' '] * 10
                
board = make_new_board()    

def make_move(board, letter, move):
    board[move] = letter

def is_free(board, space):
    return board[int(space)] == ' '

def is_won(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter))

def is_full(board):
    return ((not is_free(board, 1)) and
            (not is_free(board, 2)) and
            (not is_free(board, 3)) and
            (not is_free(board, 4)) and
            (not is_free(board, 5)) and
            (not is_free(board, 6)) and
            (not is_free(board, 7)) and
            (not is_free(board, 8)) and
            (not is_free(board, 9)))
        
    

lettermod = -1
while True:
    draw_board(board)
    lettermod += 1
    print(first_person[(lettermod % 2)] + ' is playing')
    try:
        move = int(input('what is your move (1-9)'))
    except Exception as e:
        print(f'error: {e}, restart the program.')
        
    if is_free(board, move):
        make_move(board, first_person[(lettermod % 2)], move) 
    if is_won(board, first_person[(lettermod % 2)]):
        draw_board(board)
        print(first_person[(lettermod % 2)] + ' has won!')
        break
    if is_full(board):
        print('It is a tie!')
        break

    
    

    

