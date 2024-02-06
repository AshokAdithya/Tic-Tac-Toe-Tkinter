#Tic Tac Toe using Tkinter

from tkinter import *
from tkinter import messagebox

class TicTacToe():
    def __init__(self,ttt):
        self.ttt=ttt
        self.players=['X','O']
        self.current_player = self.players[0]
        self.start_button = Button(self.ttt, text="Start", command=self.start,bg="#87CEEB",highlightthickness=0)
        self.start_button.config(font=("serif",15))
        self.start_button.pack()
        self.board=[['' for _ in range(3)]for _ in range(3)]


    def create_lines(self):
        self.canvas=Canvas(self.ttt,width=300,height=300,bg='#87CEEB',highlightthickness=0)
        self.canvas.create_line(0, 100, 300, 100, width=2)  
        self.canvas.create_line(0, 200, 300, 200, width=2)  
        self.canvas.create_line(100,0, 100, 300, width=2)  
        self.canvas.create_line(200, 0, 200, 300, width=2)

        self.canvas.pack()
    
    def start(self):
        self.start_button.pack_forget()
        self.create_lines()
        self.continue_game()

    def continue_game(self):
        self.turn_label= Label(self.ttt, text = f"{self.players[0]}'s Turn",bg="#87CEEB",pady=20)
        self.turn_label.config(font =("serif", 20,"bold"))
        self.turn_label.pack()
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        row = event.y // 100
        col = event.x // 100

        if self.current_player == 'X':
            self.draw_symbol(row, col, 'X', 'black')
        else:
            self.draw_symbol(row, col, 'O', 'black')

        if self.check_winner():
            self.show_winner()
        elif self.check_draw():
            self.show_draw()
        else:
            self.toggle_player()
    
    def check_winner(self):
        for row in self.board:
            if all(cell == row[0] and cell != '' for cell in row):
                return True
        for col in range(3):
            if all(row[col] == self.board[0][col] and self.board[0][col] != '' for row in self.board):
                return True
        if all(self.board[i][i] == self.board[0][0] and self.board[0][0] != '' for i in range(3)) or \
            all(self.board[i][2 - i] == self.board[0][2] and self.board[0][2] != '' for i in range(3)):
            return True
        return False
    def check_draw(self):
        return all(cell != '' for row in self.board for cell in row) and not self.check_winner()
    
    def show_winner(self):
        messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
        self.reset_game()
    
    def show_draw(self):
        messagebox.showinfo("Draw", "It's a draw!")
        self.reset_game()

    def draw_symbol(self, row, col, symbol, color):
        x, y = col * 100 + 50, row * 100 + 50
        self.canvas.create_text(x, y, text=symbol, font=("serif", 40, "bold"), fill=color)
        self.board[row][col] = symbol

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.turn_label.config(text=f"{self.current_player}'s Turn")

    def reset_game(self):
        self.start_button.pack()
        self.turn_label.pack_forget()
        self.canvas.pack_forget()
        self.board = [['' for _ in range(3)] for _ in range(3)]

if __name__=="__main__":
    ttt= Tk()
    window_width = 450
    window_height = 450
    screen_width = ttt.winfo_screenwidth()
    screen_height = ttt.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    ttt.geometry(f"{window_width}x{window_height}+{x}+{y}")
    ttt.title("Tic Tac Toe")
    ttt.configure(bg="#87CEEB")
    title= Label(ttt, text = "Tic Tac Toe",bg="#87CEEB",pady=20)
    title.config(font =("serif", 20,"bold"))
    title.pack()
    game=TicTacToe(ttt)

    ttt.mainloop()
