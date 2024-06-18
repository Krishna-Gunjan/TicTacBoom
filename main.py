import os
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
import numpy
import time


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.screen()
        self.geometry(f"{self.width}x{self.height}")
        self.side_frame = self.side_panel()
        self.player_details(self.side_frame)
        self.history_tab()
        self.const = 0

        self.tic_tac_toe_widget = TicTacToeWidget(master=self)
        self.tic_tac_toe_widget.place(relx=0.6, rely=0.5, anchor="center")


    def screen(self):
        self.height = self.winfo_screenheight()
        self.width = self.winfo_screenwidth()

    def side_panel(self):
        frame = ctk.CTkFrame(master=self, height=self.height, width= self.width // 8)
        frame.pack(padx=10, pady=10, side="left")
        frame.propagate(False)
        return frame

    def player_details(self, side_frame):
        player_details_frame = ctk.CTkFrame(master=side_frame,
                                            width=self.width // 8,
                                            height=self.height // 9)
        player_details_frame.pack(padx=10, pady=5)
        player_details_frame.propagate(False)

        player_label = ctk.CTkLabel(player_details_frame,
                                    text='PLAYERS', font=("Times New Roman", 16),
                                    text_color="white")
        player_label.pack()

        self.player1_label = ctk.CTkLabel(player_details_frame,
                                        text="Player 1 : X",
                                        text_color="white",
                                        width=self.width // 8,
                                        corner_radius=11,
                                        font=("Times New Roman", 20))
        self.player1_label.pack(padx=10, pady=5)
        self.player2_label = ctk.CTkLabel(player_details_frame,
                                        text="Player 2 : O",
                                        text_color="white",
                                        width=self.width // 8,
                                        corner_radius=11,
                                        font=("Times New Roman", 20))
        self.player2_label.pack(padx=10, pady=5)

    def history_tab(self):
        self.history_frame = ctk.CTkFrame(master=self.side_frame,
                                        height=600,
                                        width=200)
        self.history_frame.pack(padx=10, pady=5)
        self.history_frame.pack_propagate(False)

        history_label = ctk.CTkLabel(self.history_frame,
                                    text='HISTORY',
                                    font=('Times New Roman', 18))
        history_label.pack(padx=5, pady=1)

    def add_game_history(self, prompt):
        self.const += 1
        if self.const % 19 == 0:
            for widget in self.history_frame.winfo_children():
                widget.destroy()

            history_label = ctk.CTkLabel(self.history_frame,
                                        text='HISTORY',
                                        font=('Times New Roman', 18))
            history_label.pack(padx=5, pady=1)

        temp_label = ctk.CTkLabel(
                                  self.history_frame,
                                  text=(
                                      f"{self.const} "
                                      f"{self.tic_tac_toe_widget.current_player} "
                                      f"{prompt} the game"),
                                  font=("Times New Roman", 15)
                                  )
        temp_label.pack(padx=10, pady=1, anchor="nw")

class TicTacToeWidget(ctk.CTkFrame):
    def __init__(self, *args, master=None, **kwargs):
        super().__init__(*args, master, **kwargs)
        self.master = master
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.create_board_button()
        self.create_turn_label()

    def create_board_button(self):
        self.buttons = [[None] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = ctk.CTkButton(self,
                                                text=' ',
                                                font=('Arial', 180),
                                                text_color="black",
                                                width=200,
                                                height=200,
                                                corner_radius=0)
                self.buttons[i][j].configure(command=lambda row=i, col=j:
                                            self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=1, pady=1, sticky="nsew")

        self.active_buttons()

    def create_turn_label(self):
        self.turn_label = ctk.CTkLabel(self,
                                       text=f"Turn: Player {self.current_player}",
                                       font=("Times New Roman", 48))
        self.turn_label.grid(row=3, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].configure(text=self.current_player, state="disabled")

            if self.check_win()[0]:
                CTkMessagebox(title="You Won",
                              message=f"Congratulation! Player {self.check_win()[1]} wins",
                              icon_size=(100, 100),
                              justify="left",
                              font=("Times New Roman", 20))
                Interface.add_game_history(self.master, prompt="win")     
                self.after(1000, self.reset_game)

            elif self.check_draw():
                CTkMessagebox(title="Draw",
                            message="It is a draw",
                            icon_size=(100, 100),
                            justify="left",
                            font=("Times New Roman", 30))
                Interface.add_game_history(self.master, prompt="drew")
                self.reset_game()

            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.turn_label.configure(text=f"Turn: Player {self.current_player}")

        self.mark_changer()
        self.active_buttons()

    def check_win(self):
        
        if self.board[0][0] == self.board[0][1] == self.board[0][2] and self.board[0][0] != ' ':
            return (True, self.board[0][0])
        if self.board[1][0] == self.board[1][1] == self.board[1][2] and self.board[1][0] != ' ':
            return (True, self.board[1][0])
        if self.board[2][0] == self.board[2][1] == self.board[2][2] and self.board[2][0] != ' ':
            return (True, self.board[2][0])

        if self.board[0][0] == self.board[1][0] == self.board[2][0] and self.board[0][0] != ' ':
            return (True, self.board[0][0])
        if self.board[0][1] == self.board[1][1] == self.board[2][1] and self.board[0][1] != ' ':
            return (True, self.board[0][1])
        if self.board[0][2] == self.board[1][2] == self.board[2][2] and self.board[0][2] != ' ':
            return (True, self.board[0][2])

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return (True, self.board[0][0])
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return (True, self.board[0][2])

        return (False, None)


    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text=' ', state="normal")
                self.board[i][j] = ' '

        self.current_player = 'X'
        self.turn_label.configure(text=f"Turn: Player {self.current_player}")

    def active_buttons(self):
        trigger = 0
        for i in range(3):
            inactive_index = numpy.random.randint(0, 3, size=1)
            for j in range(3):
                if inactive_index == j:
                    self.buttons[i][j].configure(state="disabled", fg_color="red")
                    if self.board[i][j] != " ":
                        trigger += 1
                else:
                    if self.board[i][j] == " ":
                        self.buttons[i][j].configure(state="normal", fg_color="green")
                    else:
                        self.buttons[i][j].configure(fg_color="green")

        if trigger == 3:
            self.active_buttons()
        self.is_possible_moves_left()

    def is_possible_moves_left(self):
        empty_spaces_left = False
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    if self.buttons[i][j].cget("state") == "normal":
                        empty_spaces_left = True
                        break
            if empty_spaces_left:
                break

        if not empty_spaces_left:
            CTkMessagebox(title="Draw",
                        message="It is a draw",
                        icon_size=(100, 100),
                        justify="left",
                        font=("Times New Roman", 30))
            Interface.add_game_history(self.master, prompt="drew")
            self.reset_game()

    def mark_changer(self):
        choices = [True, False]
        probabilities = [0.2, 0.8]
        result = numpy.random.choice(choices, p=probabilities)
        if result:
            indicies_to_swap = numpy.random.randint(0, 3, size=2)
            if self.board[indicies_to_swap[0]][indicies_to_swap[1]] == " ":
                return
            else:
                marker = 'X' if self.board[indicies_to_swap[0]][indicies_to_swap[1]] == "O" else "O"
                self.buttons[indicies_to_swap[0]][indicies_to_swap[1]].configure(text=marker)
                self.board[indicies_to_swap[0]][indicies_to_swap[1]] = marker

            if self.check_win():
                self.reset_game()
                CTkMessagebox(title="You Won",
                            message=f"Congratulation! Player {self.current_player} wins",
                            icon_size=(100, 100),
                            justify="left",
                            font=("Times New Roman", 20))
                Interface.add_game_history(self.master, prompt="win")
                return

if __name__ == '__main__':
    interface = Interface()
    interface.mainloop()
