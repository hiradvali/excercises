from tkinter import *
from tkinter import messagebox
import random 

# tarif kardan har bazikon be soorat random

player = random.choice(['o', 'x'])
color = {'o': 'blue' , 'x': 'red'}
board =[[],[],[]]

# tabei ke bad az ahr dast etefaghat ghabli ro pak mikonad va mitavan etelaat jadid vared kard

def clear():
    global player
    global board
    for i in range (3):
        for j in range(3):
            board[i][j]["text"]= " "
            board[i][j]["state"]=NORMAL
    player = random.choice(["o","x"])

# tarif kardan sharayet bord va bakht

def click(row,col):
    global player
    global color
    global board
    board[row][col].config(text = player , state=DISABLED , disabledforeground = color[player])
    for i in range(3):
        if (board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"]==player or board[0][i]["text"]== board[1][i]["text"]== board[2][i]["text"]== player):
            messagebox.showinfo("nice", player + "won")
            clear()
        if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"]==player or board[0][2]["text"]== board[1][1]["text"]== board[2][0]["text"]== player):
            messagebox.showinfo("nice", player + "won")
            clear()
        elif (board[0][0]["state"]==board[0][1]["state"]==board[0][2]["state"]== DISABLED 
            and board[1][0]["state"]==board[1][1]["state"]==board[1][2]["state"]==DISABLED
            and board[2][0]["state"]==board[2][1]["state"]==board[2][2]["state"]==DISABLED):
            messagebox.showinfo("natije tekrari", "nobody won")
    if player=='x':
        player = 'o'
    else:
        player = 'x'
    nobat.config(text=player + "turn")
              
            
        
        
# tarif kardan mohit bazi :

tkboard=Tk()
tkboard.title("Welcome to xo game")

button_1 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(0,0))
button_1.grid(row=0,column=0)
board[0].append(button_1)

button_2 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(0,1))
button_2.grid(row=0,column=1)
board[0].append(button_2)

button_3 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(0,2))
button_3.grid(row=0,column=2)
board[0].append(button_3)

button_4 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(1,0))
button_4.grid(row=1,column=0)
board[1].append(button_4)

button_5 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(1,1))
button_5.grid(row=1,column=1)
board[1].append(button_5)

button_6 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(1,2))
button_6.grid(row=1,column=2)
board[1].append(button_6)

button_7 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(2,0))
button_7.grid(row=2,column=0)
board[2].append(button_7)

button_8 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(2,1))
button_8.grid(row=2,column=1)
board[2].append(button_8)

button_9 = Button(tkboard,text=' ',font='Times 20 bold' , bg='light gray' , height=3 , width=6 , command=lambda: click(2,2))
button_9.grid(row=2,column=2)
board[2].append(button_9)


nobat =  Label(tkboard , text=player + "bazi kone" , font='Times 20 bold')
nobat.grid(row=3, column=0, columnspan=3)
tkboard.mainloop()