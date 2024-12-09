import tkinter as tk
import random
from tkinter.messagebox import showinfo

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Крестики-Нолики")

        self.board = [""] * 9
        self.buttons = []
        self.turn = ""
        self.player_symbol = ""
        self.bot_symbol = ""

        self.create_widgets()
        self.choose_symbol()

    def create_widgets(self):
        for i in range(9):
            button = tk.Button(self.master, text="", font=("Helvetica", 50), width=5, height=2,
                               command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def choose_symbol(self):
        top = tk.Toplevel(self.master)
        top.title("X/0")
        top.geometry('+1500+200')
        top.resizable(False,False)
        
        tk.Label(top, text="За что вы хотите играть: X или O?").pack(pady=10)

        def set_symbol(symbol):
            self.player_symbol = symbol
            self.bot_symbol = "O" if symbol == "X" else "X"
            self.turn = symbol 

            top.destroy()
            self.reset_board()
            if symbol == "O":  
                self.bot_move()

        tk.Button(top, text="X", command=lambda: set_symbol("X")).pack(pady=5)
        tk.Button(top, text="O", command=lambda: set_symbol("O")).pack(pady=5)

    def make_move(self, index):
        if self.board[index] == "" and self.turn == self.player_symbol:
            self.board[index] = self.turn
            self.buttons[index].config(text=self.turn)
            if self.check_win():
                self.show_result()
            elif self.check_draw():
                self.show_result()
            else:
                self.turn = self.bot_symbol
                self.bot_move()
                if self.check_win():
                    self.show_result()
                elif self.check_draw():
                    self.show_result()
                else:
                    self.turn = self.player_symbol

    def check_win(self):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]             
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != "":
                return True
        return False

    def check_draw(self):
        return all(cell != "" for cell in self.board)

    def show_result(self):
        if self.check_win():
            winner = self.turn
            showinfo("Игра окончена!", f"Игрок {winner} победил!")
        else:
            showinfo("Игра окончена", "Ничья!")

        if tk.messagebox.askyesno("Реванш?", "Вы хотите сыграть снова?"):
            self.choose_symbol() 
        else:
            self.master.destroy()

    def reset_board(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")

    def bot_move(self):
        
        for i in range(9):
            if self.board[i] == "" and self.check_potential_win(self.bot_symbol, i):
                self.board[i] = self.bot_symbol
                self.buttons[i].config(text=self.bot_symbol)
                return
            
        for i in range(9):
            if self.board[i] == "" and self.check_potential_win(self.player_symbol, i):
                self.board[i] = self.bot_symbol
                self.buttons[i].config(text=self.bot_symbol)
                return
        
        if self.board[4] == "":
            self.board[4] = self.bot_symbol
            self.buttons[4].config(text=self.bot_symbol)
            return

        corners = [0, 2, 6, 8]
        available_corners = [corner for corner in corners if self.board[corner] == ""]
        if available_corners:
            corner = random.choice(available_corners)
            self.board[corner] = self.bot_symbol
            self.buttons[corner].config(text=self.bot_symbol)
            return

        edges = [1, 3, 5, 7]
        available_edges = [edge for edge in edges if self.board[edge] == ""]
        if available_edges:
            edge = random.choice(available_edges)
            self.board[edge] = self.bot_symbol
            self.buttons[edge].config(text=self.bot_symbol)
            return

    def check_potential_win(self, player, index):
        board_copy = self.board[:]
        board_copy[index] = player
        return self.check_win_helper(board_copy)

    def check_win_helper(self, board):
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]             
        ]
        for pattern in win_patterns:
            if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] != "":
                return True
        return False

root = tk.Tk()
root.geometry('+650+200')
game = TicTacToe(root)
root.mainloop()