import tkinter as tk
from tkinter import messagebox
import chess

# Create the main window
root = tk.Tk()
root.title("Chess Game")

# Define the board
board = chess.Board()

# Create a function to render the board
def render_board():
    for i in range(8):
        for j in range(8):
            piece = board.piece_at(chess.square(i, j))
            if piece:
                label = tk.Label(root, text=piece.unicode_symbol(), font=("Arial", 24))
                label.grid(row=i, column=j)
            else:
                label = tk.Label(root, text=" ")
                label.grid(row:i, column:j)

render_board()
root.mainloop()
