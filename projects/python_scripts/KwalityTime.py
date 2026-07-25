# KwalityTime: A collection of games to play in the terminal
import random

class TicTacToe:
    def __init__(self):
        self.board = self.make_new_board()
        self.first_person = self.who_goes_first()
        self.lettermod = -1
        print('Welcome to tic-tac-toe!')
        print('the spaces are as so:\n7|8|9\n-+-+-\n4|5|6\n-+-+-\n1|2|3')
        print('You are ' + self.first_person[0])

    def who_goes_first(self):
        if random.randint(0, 1) == 1:
            return ['X', 'O']
        else:
            return ['O', 'X']

    def draw_board(self):
        board = self.board
        print(board[7] + '|' + board[8] + '|' + board[9])
        print('-+-+-')
        print(board[4] + '|' + board[5] + '|' + board[6])
        print('-+-+-')
        print(board[1] + '|' + board[2] + '|' + board[3])

    def make_new_board(self):
        return [' '] * 10

    def make_move(self, letter, move):
        self.board[move] = letter

    def is_free(self, space):
        return self.board[int(space)] == ' '

    def is_won(self, letter):
        board = self.board
        return ((board[1] == letter and board[2] == letter and board[3] == letter) or
                (board[4] == letter and board[5] == letter and board[6] == letter) or
                (board[7] == letter and board[8] == letter and board[9] == letter) or
                (board[1] == letter and board[4] == letter and board[7] == letter) or
                (board[2] == letter and board[5] == letter and board[8] == letter) or
                (board[3] == letter and board[6] == letter and board[9] == letter) or
                (board[1] == letter and board[5] == letter and board[9] == letter) or
                (board[7] == letter and board[5] == letter and board[3] == letter))

    def is_full(self):
        return all(not self.is_free(i) for i in range(1, 10))

    def play_game(self):
        while True:
            self.draw_board()
            self.lettermod += 1
            current_player = self.first_person[self.lettermod % 2]
            print(current_player + ' is playing')
            try:
                move = int(input('What is your move (1-9)? '))
            except Exception as e:
                print(f'Error: {e}, restart the program.')
                continue

            if self.is_free(move):
                self.make_move(current_player, move)
            if self.is_won(current_player):
                self.draw_board()
                print(current_player + ' has won!')
                break
            if self.is_full():
                print('It is a tie!')
                break

# Chess game
import sys

class ChessGame:
    def __init__(self):
        self.board = self.make_board_list()
        self.create_board(self.board)
        self.turn = 'white'
        self.run_game()

    def create_board(self, board):
        print('   abcdefgh')
        print(' +----------+')
        for i in range(8):
            print(f'{i+1}| ', end='')
            for m in range(8):
                print(board[i][m], end='')
            print(f' |{i+1}')
        print(' +----------+')
        print('   abcdefgh')

    def make_board_list(self):
        return [['R','N','B','Q','K','B','N','R'],
                ['P','P','P','P','P','P','P','P'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['.','.','.','.','.','.','.','.'],
                ['p','p','p','p','p','p','p','p'],
                ['r','n','b','q','k','b','n','r']]

    def move_piece(self, move):
        try:
            # Parse input
            num1 = move[0] + move[1]
            num2 = move[2] + move[3]
            start, end = num1, num2
            start_col, start_row = ord(start[0]) - ord('a'), int(start[1]) - 1
            end_col, end_row = ord(end[0]) - ord('a'), int(end[1]) - 1

            # Validate move (basic validation)
            if self.board[start_row][start_col] == '.':
                print("Invalid move: No piece at start position")
                return

            # Move piece
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = '.'

            # Reprint board
            self.create_board(self.board)
        except Exception as e:
            print(f"Invalid move format: {e}")

    def run_game(self):
        while True:
            print(f'It is {self.turn}\'s turn')
            user_input = input("Enter your move (e.g., e2e4 aka UCI): ")
            if user_input.lower() == 'exit':
                sys.exit()
            self.move_piece(user_input)
            self.turn = 'black' if self.turn == 'white' else 'white'

# Hex speller game
import random
import sys

class HexSpeller:
    def __init__(self):
        self.board = self.fresh_board()
        self.wordslist = []
        self.score = 0
        self.run_game()

    def fresh_board(self):
        letterslist = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        board = []
        for i in range(7):
            board.append(random.choice(letterslist))
        return board

    def display_board(self):
        board = self.board
        print(f'   {board[0]}')
        print(f' {board[1]}   {board[2]}')
        print(f'   {board[3]}')
        print(f' {board[4]}   {board[5]}')
        print(f'   {board[6]}')

    def is_valid_word(self, word):
        board = self.board
        if len(word) < 3:
            return False
        elif not board[3] in word:
            return False
        else:
            for i in word:
                if not i in board:
                    return False
            return True

    def get_word(self):
        word = input('Enter a word (or q): ')
        if word == 'q':
            print(f'Your score is {self.score}, your valid words are {" ".join(self.wordslist)}')
            sys.exit()
        if self.is_valid_word(word):
            return word
        else:
            print('Invalid input, try again')
            return self.get_word()  # Ensure the function returns a valid word

    def run_game(self):
        self.display_board()
        while True:
            word = self.get_word()
            if word in self.wordslist:
                print('You already found that word')
            else:
                self.wordslist.append(word)
                self.score += 1

# Checkers game

class Checkers:
    def __init__(self):
        self.board = self.create_new_board()
        self.player = 'r'
        self.run_game()

    def create_new_board(self):
        return [['b', '.', 'b', '.', 'b', '.', 'b', '.'],
                ['.', 'b', '.', 'b', '.', 'b', '.', 'b'],
                ['b', '.', 'b', '.', 'b', '.', 'b', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', 'r', '.', 'r', '.', 'r', '.', 'r'],
                ['r', '.', 'r', '.', 'r', '.', 'r', '.'],
                ['.', 'r', '.', 'r', '.', 'r', '.', 'r']]

    def print_board(self):
        print('  0 1 2 3 4 5 6 7')
        for i in range(8):
            print(i, end=' ')
            for j in range(8):
                print(self.board[i][j], end=' ')
            print()

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        if self.board[start_row][start_col] == '.':
            return False
        if self.board[end_row][end_col] != '.':
            return False
        if self.player == 'r':
            if start_row >= end_row:
                return False
        if self.player == 'b':
            if start_row <= end_row:
                return False
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        if abs(start_row - end_row) > 2:
            return False
        if abs(start_row - end_row) == 2:
            if self.board[(start_row + end_row) // 2][(start_col + end_col) // 2] == '.':
                return False
            if self.board[(start_row + end_row) // 2][(start_col + end_col) // 2].lower() == self.player:
                return False
        return True

    def make_move(self, start_row, start_col, end_row, end_col):
        if self.is_valid_move(start_row, start_col, end_row, end_col):
            self.board[end_row][end_col] = self.board[start_row][start_col]
            self.board[start_row][start_col] = '.'
            if abs(start_row - end_row) == 2:
                self.board[(start_row + end_row) // 2][(start_col + end_col) // 2] = '.'

    def run_game(self):
        while True:
            self.print_board()
            print('Player', self.player)
            try:
                start_row = int(input('Enter start row: '))
                start_col = int(input('Enter start col: '))
                end_row = int(input('Enter end row: '))
                end_col = int(input('Enter end col: '))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if self.is_valid_move(start_row, start_col, end_row, end_col):
                self.make_move(start_row, start_col, end_row, end_col)
                self.player = 'b' if self.player == 'r' else 'r'
            else:
                print('Invalid move')

if __name__ == "__main__":
    print('Welcome to KwalityTime!')
    print('1. Tic Tac Toe')
    print('2. Chess')
    print('3. Hex Speller')
    print('4. Checkers')
    choice = input('Enter the number of the game you want to play: ')
    if choice == '1':
        TicTacToe().play_game()
    elif choice == '2':
        ChessGame()
    elif choice == '3':
        HexSpeller()
    elif choice == '4':
        Checkers().run_game()
    else:
        print('Invalid choice')
        sys.exit()
    