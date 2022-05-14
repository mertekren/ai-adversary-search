"""
todo list:
1) change minimax function a bit so that it's not same

"""
import sys
from math import inf
from curses.ascii import isdigit

class Puzzle:
    horizontal_len=0
    vertical_len=0
    next_robot_list = []
    current_player=0
    current_player_idx=0
    game_over_flag=0
    current_player_i_j = (0,0)
    def __init__(self, lines):        
        n = len(lines)
        self.horizontal_len = len(lines[0])-1
        self.vertical_len = len(lines)
        
        for i in range (self.vertical_len):
            for j in range(self.horizontal_len):                            
                if(lines[i][j] == 'c'):
                    self.next_robot_list.append(0)
                elif(isdigit(lines[i][j])):
                    self.next_robot_list.append(int(lines[i][j]))
                else:
                    continue
        
        self.next_robot_list = sorted(self.next_robot_list)
    
    def find_next_Robot(self):
        if(self.current_player_idx == puzzle.next_robot_list.__len__()):
            self.current_player_idx = 0
            self.current_player = 0 
        
        else
            self.current_player_idx++
            self.current_player = self.next_robot_list[self.current_player_idx] 
        
    def is_game_over(self):
        if(self.game_over_flag):
            return 1
        else:
            return 0
    
    def find_neighbors(self):
        list = []
        
        
        
    def minimax(self):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """       
        if self.current_player == 0:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]
    
        if self.is_game_over():
            score = evaluate()
            return [-1, -1, score]
    
        neighbor_cells = self.find_neighbors()
        for cell in empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = minimax(state, depth - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y
    
            if player == COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
    
        return best
        
if(sys.argv[1] != "min-max" and sys.argv[1] != "alpha-beta"):
    exit

with open(sys.argv[2]) as f:
    lines = f.readlines()      

puzzle = Puzzle(lines)
puzzle.minimax()

print(lines)