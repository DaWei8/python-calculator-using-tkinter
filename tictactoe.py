from email.policy import default
import tkinter as tk


player_switch = True
player = ""
player_turn = "Player X turn"
game_won = False



post_1 = " "
post_2 = " "
post_3 = " "
post_4 = " "
post_5 = " "
post_6 = " "
post_7 = " "
post_8 = " "
post_9 = " "


btn_post = {
    post_1: "", post_2: "", post_3: "",
    post_4: "", post_5: "", post_6: "",
    post_7: "", post_8: "", post_9: "",
}


def switch_player():
    global player_switch
    global player
    
    if player_switch is True:
        player = "X"
    else:
        player = "O"

    player_switch = not player_switch
    return player


def choose_position(position):

    position = switch_player()
    print("you chose position " + position)


def restart_game():
    # reset all values
    pass


def start_game():
    global player_turn
    global root
    root = tk.Tk()
    root.geometry()
    # display a prompt to choose
    # player X/y goes first
    # check if player x/y has won
    # if player x/y has won, end game
    # else switch player


    pass


def check_win():
    pass


def end_game():
    pass



start_game()
row = 1
tk.Variable(root, value="Banana")

text_game_info = tk.Text(root, font=("Arial", 24), width=9, height=2 )
text_game_info.grid(row=1,column = 1, columnspan=3)

btn_1 = tk.Button(root, text=post_1, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_1.grid(row=row + 1, column=1)

btn_2 = tk.Button(root, text=post_2, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_2.grid(row=row + 1, column=2)

btn_3 = tk.Button(root, text=post_3, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_3.grid(row=row + 1, column=3)

btn_4 = tk.Button(root, text=post_4, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_4.grid(row=row + 2, column=1)

btn_5 = tk.Button(root, text=post_5, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_5.grid(row=row + 2, column=2)

btn_6 = tk.Button(root, text=post_6, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_6.grid(row=row + 2, column=3)

btn_7 = tk.Button(root, text=post_7, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_7.grid(row=row + 3, column=1)

btn_8 = tk.Button(root, text=post_8, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_8.grid(row=row + 3, column=2)

btn_9 = tk.Button(root, text=post_9, command=lambda: choose_position(btn_post[post_1]), width=4, font=("Arial", 14))
btn_9.grid(row=row + 3, column=3)

btn_restart = tk.Button(root, text="Restart ", command=lambda: restart_game, width=14, font=("Arial", 14))
btn_restart.grid(row= row + 4,column=1, columnspan=3 , )


root.mainloop()
