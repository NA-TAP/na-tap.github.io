# Hex speller game
import random
import sys

def fresh_board():
    letterslist = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    board = []
    for i in range(7):
        board.append(random.choice(letterslist))
    return board

def display_board(board):
    print(f'   {board[0]}')
    print(f' {board[1]}    {board[2]}')
    print(f'   {board[3]}')
    print(f' {board[4]}    {board[5]}')
    print(f'   {board[6]}')

def is_valid_word(word, board):
    if len(word) < 3:
        return False
    elif not board[3] in word:
        return False
    else:
        for i in word:
            if not i in board:
                return False
        return True

def get_word(board, score, words):
    word = input('Enter a word (or q): ')
    if word == 'q':
        print(f'Your score is {score}, your valid words are {' '.join(words)}')
        sys.exit()
    if is_valid_word(word, board):
        return word
    
    else:
        print('Invalid input, try again')
        return get_word(board, score)  # Ensure the function returns a valid word

def main():
    wordslist=[]
    board = fresh_board()
    display_board(board)
    score = 0
    while True:
        word = get_word(board, score, wordslist)
        if word in wordslist:
            print('You already found that word')
        else:
            wordslist.append(word)
        score += 1

if __name__ == "__main__":
    main()