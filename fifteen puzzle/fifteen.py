# assignment: PA5: Fifteen
# author: Aidan Au-Yeung
# date: 12/01/22
# file: Code for the game fifteen 
# input: potential moves to rearange the game in the right order
# output: rearanged board based on input

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.size = size
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.adj = [[1,4],[0,2,5],[1,3,6],[2,7],[0,5,8],[1,4,6,9],[2,5,7,10],[3,6,11],[4,9,12],[5,8,10,13],[6,9,11,14],[7,10,15],[8,13],[9,12,14],[10,13,15],[11,14]]

    #shifts the board based on the input move if the move is in zero's self.adj
    def update(self, move):
        if np.where(self.tiles == move)[0][0] in self.adj[np.where(self.tiles==0)[0][0]]:
            index_mt = np.where(self.tiles == 0)[0][0]
            index = np.where(self.tiles == move)[0][0]
            self.tiles[index_mt] = move
            self.tiles[index] = 0
        else:
            pass

    #not sure if we needed this lmk
    def transpose(self, i, j):
        pass

    #shuffles the board steps amount of times
    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for i in range(steps):
            move_index = choice (self.adj[index])
            self.tiles[index],self.tiles[move_index] = self.tiles[move_index],self.tiles[index]
            index = move_index
        
    #checks if the input move is adjacent to zero's current position    
    def is_valid_move(self, move):
        empty = np.where(self.tiles == 0)[0][0]
        try:
            if self.tiles[empty + 1] == move:
                return True
        except:
            pass
        try:
            if self.tiles[empty - 1] == move:
                return True
        except:
            pass
        try:
            if self.tiles[empty - 4] == move:
                return True
        except:
            pass
        try:
            if self.tiles[empty + 4] == move:
                return True
        except:
            pass
        return False

    #checks if the board is arranged from 1-15 with zero at the end
    def is_solved(self):
        solution = np.array([i for i in range(1,self.size**2)] + [0])
        if np.array_equal(solution,self.tiles):
            return True
        return False

    #prints out the board in a nice little interface on terminal
    def draw(self):
        tiles = []
        for tile in self.tiles:
            if int(tile) < 10:
                spacer = f' {tile} '
            else:
                spacer = f'{tile} '
            tiles.append(spacer)
            
        out = f"""
+---+---+---+---+
|{tiles[0]}|{tiles[1]}|{tiles[2]}|{tiles[3]}|
+---+---+---+---+
|{tiles[4]}|{tiles[5]}|{tiles[6]}|{tiles[7]}|
+---+---+---+---+
|{tiles[8]}|{tiles[9]}|{tiles[10]}|{tiles[11]}|
+---+---+---+---+
|{tiles[12]}|{tiles[13]}|{tiles[14]}|{tiles[15]}|
+---+---+---+---+
        """
        print(out)
    
    
    def __str__(self):
        out = ''
        for i in range(len(self.tiles)):
            if int(self.tiles[i]) == 0:
                out += '   '
            else:
                if int(i) < 9:
                    out += ' '
                out += str(self.tiles[i])
                out += ' '
            if (i+1) % 4 == 0 and i != 0:
                out += '\n'
        return out

    
if __name__ == '__main__':
    
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)

    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
    
    
    # #You should be able to play the game if you uncomment the code below'''
    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')