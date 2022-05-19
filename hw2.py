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
    #current_player=0
    current_player_idx=0
    game_over_flag=0
    current_player_i_j = (0,0)
    cleanzone = []
    initial_cleaner_position=(0,0)
    max_cleaner_idx=0
    
    num_of_dirts_cleaner=0
    num_of_dirts_opponent=0
    
    def __init__(self, lines):        
        n = len(lines)
        self.horizontal_len = len(lines[0])-1
        self.vertical_len   = len(lines)
        
        #self.cleanzone = lines #maybe additional edits
        
        #find all players and order them
        for i in range (self.vertical_len):
            for j in range(self.horizontal_len):                            
                if(lines[i][j] == 'c'):
                    self.next_robot_list.append(0)
                    self.initial_cleaner_position = (i,j)
                    self.max_cleaner_idx += 1
                elif(isdigit(lines[i][j])):
                    self.next_robot_list.append(int(lines[i][j]))
                    self.max_cleaner_idx += 1
                else:
                    continue        
        self.next_robot_list = sorted(self.next_robot_list)
                
    def find_next_Robot(self):
        if(self.current_player_idx == puzzle.next_robot_list.__len__()):
            self.current_player_idx = 0
            self.current_player = 0 
        
        else
            self.current_player_idx += 1
            self.current_player = self.next_robot_list[self.current_player_idx] 
        
    def is_game_over(self):
        if(self.game_over_flag):
            return 1
        else:
            return 0
    
    def find_neighbors(self, cleaner_position):
        list = []
        (_x, _y) = cleaner_position
        #If required, the precedence used as a tie-breaker is as follows: left, right, down, up, stop, suck
        #bu ustte de tam anlamadigim bisiyler var.
        #left
        self.add_tile(list, _x-1, _y, 'left')        
        #right
        self.add_tile(list, _x+1, _y, 'right')
        #down
        self.add_tile(list, _x, _y+1, 'down')
        #up
        self.add_tile(list, _x, _y-1, 'up')
        #stop
        self.add_tile(list, _x, _y, 'stop')
        #suck
        self.add_tile(list, _x, _y, 'suck')                                                    
        
    def add_tile(self, list, x, y, move):
        current_tile = self.cleanzone[x][y]
        if current_tile == 'x'
            continue
        elif current_tile = '.'
            list.append(move, x, y, 1)
        elif isdigit(current_tile)
            list.append(move, x, y, -100)
        
    #def util_func(self): To-do
                
        
        
    def minimax(self, cleanzone, cleaner_position, cleaner_idx):
        """
        AI function that choice the best move
        :param state: current state of the board
        :param depth: node index in the tree (0 <= depth <= 9),
        but never nine in this case (see iaturn() function)
        :param player: an human or a computer
        :return: a list with [the best row, best col, best score]
        """       
        if cleaner_idx == self.max_cleaner_idx:
            cleaner_idx = 0
        
        if cleaner_idx == 0:
            best = [-1, -1, -inf]            
        else:
            best = [-1, -1, +inf]            
    
        if self.is_game_over():
            score = evaluate()
            return [-1, -1, score]
        
        (_x, _y) = cleaner_position
        neighbor_cells = self.find_neighbors(cleaner_position) #TODO: actions might be better name here
        for cell in neighbor_cells:
            x, y, move = cell[1], cell[2], cell[3]
            self.increment_cleanzone(cleanzone, (),(x, y), move)
            score = self.minimax(cleanzone, (x,y), cleaner_idx+1)
            
            score[0], score[1] = x, y
    
            if player == COMP:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value
    
        return best
    
    def increment_cleanzone(self, cleanzone, (_x, _y), (x, y), move):
        if cleanzone[x][y] == 'c':
            print("error 1\n")                 
        elif cleanzone[x][y] == 'x':
            print("error 2\n")     
        elif cleanzone[x][y] == '.':
            
        elif isdigit(cleanzone[x][y]):
            print("error 1\n")   
        elif cleanzone[x][y] == ' ':
            print("error 1\n")     
               
if(sys.argv[1] != "min-max" and sys.argv[1] != "alpha-beta"):
    exit

with open(sys.argv[2]) as f:
    lines = f.readlines()      

puzzle = Puzzle(lines)
puzzle.minimax(lines, puzzle.initial_cleaner_position, 0)

print(lines)