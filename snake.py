"""
This program is a snake game.
Made with the help of TK Inter library.
The snake in this game only moves and does not increase in size. 
"""
from tkinter import *



window = Tk()
window.title('Snake')          # we open the Tk module and put it in some variable like window
window['height'] = 400
window['width'] = 400#________________
#  / we set the height and width here \ 


window_2 = Canvas(window)  # To make a square, we need the canvas module
filler = window_2.create_rectangle(10,20,30,40)
window_2.grid(row=0 , column=0)    # for start the game from [0,0] we needed to set row and column to 0



def move_snake(thing):
    """
    Snake moves with w,a,s,d buttons 
    """

    # we have to set the default position of our snake
    x = 0
    y = 0


    if thing.char == 'a':       #|
        x -= 5                  #|
    if thing.char == 'd':       # \
        x +=5                   #  >>>      we set w,a,s,d for move +-5 here  
    if thing.char == 's':       # /
        y +=5                   #|    
    if thing.char == 'w':       #|
        y -=5                   #|            


    window_2.move(filler, x, y)          # for apply the moves , we have to use move module and call our variable
    

window.bind('<Key>',move_snake) # '<Key>' is a type of variale like : abcdefghigklmnop...   
# then , we have to call our function
window.mainloop()
# and finlly we can run our code with calling our window , and ( .mainloop )



"""

if you use vscode , just click on "run python file"
if you use a text editor,you have to do : right-click then click on run python file in terminall
*** enjoy the game ***


"""