import random
#player class with for manual play
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
    #returns player object's sign
      def get_sign(self):
            return self.sign
    #return player object's name
      def get_name(self):
            return self.name
    #asks player for a coordinate to mark the board with sign
      def choose(self, board):
            valid = False
            trie = input("\n" + self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:\n")
            trie = trie.upper()
            while valid == False:    
                  valid_inputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
                  if trie in valid_inputs and board.isempty(trie):
                        board.set(trie,self.sign)
                        valid_inputs.remove(trie)
                        valid = True            
                  else:
                        print('\nYou did not choose correctly.')
                        trie = input("\n" + self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:\n")
                        trie = trie.upper()


            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)

#Random AI class that randomly selects spaces on the board when played against
class AI(Player):
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X

    #Randomly chooses an open space to mark when called
      def choose(self,board):
            print(self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:\n")
            valid_inputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
            input = random.choice(valid_inputs)
            valid = False
            while valid == False:
                  if input in valid_inputs and board.isempty(input):
                        board.set(input,self.sign)
                        valid_inputs.remove(input)
                        valid = True
                  else:
                        input = random.choice(valid_inputs)

#Class is a smarter AI that recursively calls the minimax algorithm to never lose.
class MiniMax(AI):
    def choose(self, board): 
        print(self.name + ", " + self.sign + ": Enter a cell [A-C][1-3]:\n")
        move = self.minimax(board,True,True)
        board.set(move,self.sign)

    #minimax algorithm that compares possible outcomes by simulating possible ways the game could go
    def minimax(self,board,self_player,start):
        index = ["A1","B1","C1","A2","B2","C2","A3","B3","C3"]
        min = 1000
        max = -1000
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1
            elif board.get_winner() == '':
                return 0
            else:
                return -1
        for cell in index:
            if board.isempty(cell):
                if self_player:
                    board.set(cell,self.sign)
                    eval = self.minimax( board, False, False)
                    board.undo(cell)

                    if eval > max:
                        max = eval
                        best = cell
                else:
                    opp = "X"
                    if self.sign == opp:
                        opp = "O"
                    board.set(cell,opp)
                    eval = self.minimax(board,True,False)
                    board.undo(cell)
                    if eval < min:
                            min = eval
                            best = cell
        if start:
            return best
        elif self_player:
            return max
        else:
            return min

#WIP SmartAI that takes a heuristic approach to tic tac toe to never lose. 
# It doesnt work.               
# class SmartAI(AI):
#     def __init__(self, name, sign):
#             self.name = name  # player's name
#             self.sign = sign  # player's sign O or X
#             self.optimal = None

#     def lf_combo (self,board,sign):
#         self.optimal = None
#         index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8}
#         index_wins = [['A1','B1','C1'],['A2','B2','C2'],['A3','B3','C3'],['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3'],['A1','B2','C3'],['A3','B2','C1']]
#         wins = [[board.board[0],board.board[1],board.board[2]],[board.board[3],board.board[4],board.board[5]],[board.board[6],board.board[7],board.board[8]],[board.board[0],board.board[3],board.board[6]],[board.board[1],board.board[4],board.board[7]],[board.board[2],board.board[5],board.board[8]],[board.board[0],board.board[4],board.board[8]],[board.board[6],board.board[4],board.board[2]]]
#         ind = 0
#         for set in wins:
#             combo = 0
#             empty = 0
#             for cell in set:
#                 if cell == sign:
#                     combo += 1
#                 if cell == ' ':
#                     empty += 1
#             if combo == 2 and empty == 1:
#                 save = set.index(' ')
#                 self.optimal = index_wins[ind][save]
#                 return 2
#             if combo == 1 and empty == 2:
#                 save = set.index(' ')
#                 print(ind,save)
#                 print(index_wins)
#                 self.optimal = index_wins[ind][save]
#                 return 1
#             ind += 1
#         return False
    
#     def first(self,board):
#         index = {'A1':0,'B1':1,'C1':2,'A2':3,'B2':4,'C2':5,'A3':6,'B3':7,'C3':8} 
#         first = True
#         for cell in index:
#             if board.isempty(cell):
#                 first = False
#         return first

#     def options(self,board):
#         option_lst = []
#         index = ['A1','B1','C1','A2','B2','C2','A3','B3','C3'] 
#         for cell in index:
#             if board.isempty(cell):
#                 option_lst.append(cell)
#         return option_lst

#     def choose(self,board):

#         moves = self.options(board)
#         prioritize = ['B2','A1','C1','A3','C3',]
#         opp = 'X' if self.sign == 'O' else 'O'
#         print(opp)
#         print(self.lf_combo(board,self.sign))
#         print(self.lf_combo(board,opp))
#         if self.lf_combo(board,self.sign) == 2:
#             print('ATAAAACK')
#             board.set(self.optimal,self.sign)
#             return 

#         if self.lf_combo(board,opp) == 2:
#             print('BLOCKKKKK')
#             board.set(self.optimal,self.sign)
#             return

#         if len(moves) == 9:
#             print("MIIIIDLE")
#             board.set('B2',self.sign)
#             return

#         for cell in prioritize:
#             if cell in moves:
#                 if self.lf_combo(board,self.sign) == 1:
#                     print("OFFENSIVE")
#                     board.set(cell,self.sign)
#                     return
#                 else:
#                     print("PRIORITIZE BUT RANDOOOM")
#                     board.set(cell,self.sign)
#                     return

#         input = random.choice(moves) 
#         print("OOOPS SOMETHING WENT WRONG Q.Q")       
#         board.set(input,'T')
#         return
        
        


        
        


