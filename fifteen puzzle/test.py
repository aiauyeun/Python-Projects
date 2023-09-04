from tkinter import *
from fifteen import Fifteen
tiles = Fifteen() 
class BattleScreen(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)

        shwarma = []
        for i in range(len(tiles.tiles)):
            if tiles.tiles[i] != 0:
                shwarma.append(Button(gui, textvariable =text,name = str(pos),bg='red',fg='black', height=5, width=5, command = lambda: clickButton(int(pos)))
            else:
                shwarma.append(addButton(gui,tiles.tiles[i],tiles.tiles[i]))
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


class Controls(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.quit = Button(self, text="Quit", width=6, 
                           command=root.destroy)
        self.quit.pack()

root = Tk()
screen = BattleScreen(root)
controls = Controls(root)
controls.pack(side="bottom", fill="x")
screen.pack(side="top", fill="both", expand=True)
root.mainloop()