#Board object sets up a 3x3 tic tac toe board that can be modified
class Board:
    def __init__(self):
        # board is a list of cells that are represented 
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented 
        # by " " strings
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        # the winner's sign O or X
        self.winner = ""
    
    #returns the size of the board 
    def get_size(self): 
        return self.size

    #returns self.winner    
    def get_winner(self):
        return self.winner
        # return the winner's sign O or X (an instance winner)    

    def get_sign(self,cell):
        index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}
        return self.board[index[cell]]


    #marks the cell on the board with the sign X or O        
    def set(self, cell, sign):
        index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}
        if cell in index:
            self.board[index[cell]] = sign
            

    #Returns True if the target sell in self.board is empty
    def isempty(self, cell):
        index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}
        if cell in index:
            if self.board[index[cell]] == ' ':
                return True
            else:
                return False

    # check all game terminating conditions, if one of them is present, assign the var done to True
    # depending on conditions assign the instance var winner to O or X
    def isdone(self):
        done = False
        self.winner = ''
        wins = [[self.board[0],self.board[1],self.board[2]],[self.board[3],self.board[4],self.board[5]],[self.board[6],self.board[7],self.board[8]],[self.board[0],self.board[3],self.board[6]],[self.board[1],self.board[4],self.board[7]],[self.board[2],self.board[5],self.board[8]],[self.board[0],self.board[4],self.board[8]],[self.board[6],self.board[4],self.board[2]]]

        for set in wins:
            if set[0] == set[1] == set[2] and set[0] != ' ':
                done = True
                self.winner = str(set[0])
                return done
        if ' ' not in self.board:
            done = True
        return done




    #sets the target cell equal to ' '        
    def undo(self,cell):
        index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}
        if cell in index:
            self.board[index[cell]] = ' '

    #prints out a tic tac toe table!
    def show(self):
        rows = ['1','|',' ',self.board[0],' ','|',' ',self.board[1],' ','|',' ',self.board[2],' ','|'],['2','|',' ',self.board[3],' ','|',' ',self.board[4],' ','|',' ',self.board[5],' ','|'],['3','|',' ',self.board[6],' ','|',' ',self.board[7],' ','|',' ',self.board[8],' ','|']
        tbl = """   
%s
 +---+---+---+
%s
 +---+---+---+
%s
 +---+---+---+
            """ % (''.join(rows[0]),''.join(rows[1]),''.join(rows[2]))
        print("""
   A   B   C
 +---+---+---+""")
        print(tbl.strip())

        

        
            