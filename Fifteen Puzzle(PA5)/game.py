# assignment: PA5: Fifteen
# author: Aidan Au-Yeung
# date: 12/01/22
# file: GUI interface of the fifteen game with a shuffle button 
# input: clicks 
# output: rearanged board based on input shuffles if you click the shuffle button!

from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


#shuffles the board
def shuffle():
    controls.shuffle.configure(text = 'Shuffle')
    tiles.shuffle()
    update()    

#used for added buttons onto the main fifteen grid
def addButton(gui, value,pos):
    text = StringVar()
    text.set(str(value))
    return Button(gui, textvariable =text,name = str(pos),bg='red',fg='black', height=5, width=5, command = lambda: clickButton(int(pos)))

#updates the board to reflect tiles.tiles
def update():
    shwarma = []
    for i in range(len(tiles.tiles)):
        if tiles.tiles[i] != 0:
            shwarma.append(addButton(main,tiles.tiles[i],tiles.tiles[i]))
        else:
            shwarma.append(addButton(main,tiles.tiles[i],tiles.tiles[i]))
    for i in range(len(tiles.tiles)):
        rw = 0
        clm = i % 4
        if i > 3:
            rw += 1
        if i > 7:
            rw += 1
        if i > 11:
            rw += 1
        shwarma[i].grid(row= rw, column = clm)   
        if shwarma[i].cget('text') == '0':
            shwarma[i].grid_forget()
    if tiles.is_solved():
        controls.shuffle.configure(text = 'You Won! Click here to shuffle again!')

#command that runs upon the click of the main board buttons
def clickButton(value):
        tiles.update(value)
        update()

#Frame for the main fifteen game
class MainGame(Frame):
    def __init__(self, gui):
        Frame.__init__(self, gui)

        shwarma = []
        for i in range(len(tiles.tiles)):
            if tiles.tiles[i] != 0:
                shwarma.append(addButton(self,tiles.tiles[i],tiles.tiles[i]))
            else:
                shwarma.append(addButton(self,tiles.tiles[i],tiles.tiles[i]))
        for i in range(len(tiles.tiles)):
            rw = 0
            clm = i % 4
            if i > 3:
                rw += 1
            if i > 7:
                rw += 1
            if i > 11:
                rw += 1 
            shwarma[i].grid(row= rw, column = clm)  
            if shwarma[i].cget('text') == '0':
                shwarma[i].grid_forget()
    
#class for the extra buttons of fifteen like the shuffle button
class Controls(Frame):
    def __init__(self,gui):
        Frame.__init__(self, gui)
        self.shuffle = Button(self, text="Shuffle", width=32, height= 4, 
                        command=lambda: shuffle())
        self.shuffle.pack()   
    



        

            
#main code for fifteen gui interface    
if __name__ == '__main__':
    # make tiles
    tiles = Fifteen() 
    # makes gui   
    gui = Tk()
    gui.title("Fifteen")
    #makes the main and control frame then packs them together
    main = MainGame(gui)
    controls = Controls(gui)
    controls.pack(side="bottom", fill="x")
    main.pack(side="top", fill="both", expand=True)



    
    gui.mainloop()
