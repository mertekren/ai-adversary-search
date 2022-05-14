'''
Mert ekren

hw-i


eksiklikler:
a* search 
problems with multiple goals
'''
import sys
import copy
from collections import deque
from math import inf
from curses.ascii import isdigit

def findMatrixIndex(i, j, len):
    return i*len + j

class Puzzle:     
    the_path = []
    next_robot_list = []
    
    def __init__(self, vertical_len, horizontal_len):        
        self.ArrayStates = {}
        self.num_of_dirts = 0
        self.vertical_len = vertical_len
        self.horizontal_len = horizontal_len
    
    def construct_cleaners(self, lines):    
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
        
    def count_the_dirts(self):
        #TODO for those >1    
        for i in range (self.vertical_len):
            for j in range (self.horizontal_len):
                character = lines[i][j]
                if(character.isdigit() == True): 
                    dirts_in_state = int(character)
                    self.num_of_dirts += dirts_in_state
    def isclean(self, current_num_of_dirts):
            if(self.num_of_dirts == current_num_of_dirts):
                return True
            return False
        
    #def __init__(self):  
    def constructStates(self, lines):
        global s
        
        for i in range (self.vertical_len):
            for j in range (self.horizontal_len):
                matrix_index = i*(horizontal_len) + j
                character = lines[i][j]
                if(character == 'x'):
                    continue
                # TODO ascii check here
                elif(character.isdigit() == True):            
                    # TODO: need optimization
                    '''
                    dirts_in_state = int(character)
                    stateID = "0_Dirt_%s" %matrix_index               
                    s = State(stateID)   
                    for x in range(dirts_in_state):
                        # add suck neighbor
                        move = "suck"                    
                        cost = 5                                        
                        neighbor_stateID = "%d_Dirt_%s" %(x, matrix_index)
                        b = Branches(cost, neighbor_stateID, move)                    
                        s.ArrayBranches.append(b) # add as dirt neighbor      
                        n = State(neighbor_stateID)               
                        n.num_of_dirts = 1     
                        self.ArrayStates[neighbor_stateID] = n
                    '''
                    dirts_in_state = int(character)
                    for x in range(dirts_in_state+1):
                        # add suck neighbor
                        if(x == 0):
                            stateID = "0_Dirt_%s" %matrix_index                                                         
                            s = State(stateID)
                            continue
                        self.ArrayStates[stateID] = s                                                                                               
                        s.num_of_dirts = 1 
                        stateID = "%d_Dirt_%s" %(x, matrix_index)                               
                        neighbor_stateID = "%d_Dirt_%s" %(x-1, matrix_index)
                        s = State(stateID)    
                        move = "suck"                    
                        cost = 5                                                                
                        b = Branches(cost, neighbor_stateID, move)                    
                        s.ArrayBranches.append(b) # add as dirt neighbor
                
                                                         
                    s.num_of_dirts = 0
                                                    
                elif(character == ' ' or character == 'c'):
                    stateID = "0_Dirt_%s" %matrix_index
                    s = State(stateID)
                    #append to pool
                elif(character == 'j'):
                    continue                                     
                #----------------------------------------construct neighbors
                #left ++++++++++++++++++++++++++++++++++++++++++++
                cost = 1
                move = "left"
                neighbor_index = lines[i][j-1] 
                neighbor_matrix_index = findMatrixIndex(i, j-1, self.horizontal_len)
                
                if(neighbor_index == 'j'):
                    if(j-2 >= 0):                                    
                        neighbor_index = lines[i][j-2] 
                        neighbor_matrix_index = findMatrixIndex(i, j-2, self.horizontal_len)
                    
                if(neighbor_index == ' ' or neighbor_index == 'c' ):                                                    
                    neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s                    
                    
                elif(neighbor_index.isdigit() == True):
                    neighbor_index_int = int(neighbor_index)                    
                    neighbor_stateID = "%d_Dirt_%s" %(neighbor_index_int,neighbor_matrix_index)
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s 
                #right ++++++++++++++++++++++++++++++++++++++++++++
                move = "right"
                cost = 1
                neighbor_index = lines[i][j+1] 
                neighbor_matrix_index = findMatrixIndex(i, j+1, self.horizontal_len)
                
                if(neighbor_index == 'j'):
                    if(j+2 < self.horizontal_len):               
                        neighbor_index = lines[i][j+2]                     
                        neighbor_matrix_index = findMatrixIndex(i, j+2, self.horizontal_len)
                        neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    
                if(neighbor_index == ' ' or neighbor_index == 'c' ):                                                    
                    neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s                    
                    
                elif(neighbor_index.isdigit() == True):
                    neighbor_index_int = int(neighbor_index)                    
                    neighbor_stateID = "%d_Dirt_%s" %(neighbor_index_int,neighbor_matrix_index)
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s 
                
                #down ++++++++++++++++++++++++++++++++++++++++++++
                move = "down"
                cost = 1
                neighbor_index = lines[i+1][j] 
                neighbor_matrix_index = findMatrixIndex(i+1, j, self.horizontal_len)
                
                if(neighbor_index == 'j'):
                    if(i+2 < vertical_len):                
                        neighbor_index = lines[i+2][j] 
                        neighbor_matrix_index = findMatrixIndex(i+2, j, self.horizontal_len)
                        neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    
                if(neighbor_index == ' ' or neighbor_index == 'c' ):                                                    
                    neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s                    
                    
                elif(neighbor_index.isdigit() == True):
                    neighbor_index_int = int(neighbor_index)                    
                    neighbor_stateID = "%d_Dirt_%s" %(neighbor_index_int,neighbor_matrix_index)
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s 
                #up ++++++++++++++++++++++++++++++++++++++++++++
                move = "up"
                cost = 1
                neighbor_index = lines[i-1][j] 
                neighbor_matrix_index = findMatrixIndex(i-1, j, self.horizontal_len)
                
                if(neighbor_index == 'j'):                
                    if(i-2 >= 0):
                        neighbor_index = lines[i-2][j] 
                        neighbor_matrix_index = findMatrixIndex(i-2, j, self.horizontal_len)
                        neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    
                if(neighbor_index == ' ' or neighbor_index == 'c' ):                                                    
                    neighbor_stateID = "0_Dirt_%s" %neighbor_matrix_index
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s                    
                    
                elif(neighbor_index.isdigit() == True):
                    neighbor_index_int = int(neighbor_index)                    
                    neighbor_stateID = "%d_Dirt_%s" %(neighbor_index_int,neighbor_matrix_index)
                    b = Branches(cost, neighbor_stateID, move)
                    s.ArrayBranches.append(b)       
                    self.ArrayStates[stateID] = s                                                                                        

def printCost(path3):
    cost = 0
    for i in path3:
        if(i == 'left' or i == 'right'):
            cost += 1         
        elif(i == 'up' or i == 'down'):
            cost += 2
        elif(i == 'suck'):
            cost += 5 
            
    print("cost of the solution: %d" % cost)            
class State:

    def __init__(self, ID):            
        self.ArrayBranches = []
        self.ID = ID
        self.explored = 0
        self.num_of_dirts = 0
        self.visited = 0
    
class Branches:
    def __init__(self, cost, stateID, move):
        self.cost = cost
        self.stateID = stateID 
        self.move = move      
        
# Create initial state
def findCleaner(lines):
    for i in range (len(lines)):
        for j in range (len(lines[0])-1):
            if(lines[i][j]=='c'):
                return [i,j]
    #TODO: ifnot found put error

#def findGoalStates(lines):
    
def find_next_Robot(self):
    if(self.current_player_idx == puzzle.next_robot_list.__len__()):
        self.current_player_idx = 0
        self.current_player = 0 
                              
with open(sys.argv[2]) as f:
    lines = f.readlines()
n = len(lines)
horizontal_len = len(lines[0])-1
vertical_len = len(lines) 

init = []

[cleaner_x, cleaner_y] = findCleaner(lines)
puzzle = Puzzle(vertical_len, horizontal_len)
puzzle.construct_cleaners(lines)
puzzle.constructStates(lines)
puzzle.count_the_dirts()
#puzzle.bfs(cleaner_x, cleaner_y, horizontal_len)
#puzzle.dfs(cleaner_x, cleaner_y, horizontal_len)

if(sys.argv[1] == "bfs"):
    puzzle.bfs(cleaner_x, cleaner_y, horizontal_len)
elif(sys.argv[1] == "dfs"):
    puzzle.dfs(cleaner_x, cleaner_y, horizontal_len)
elif(sys.argv[1] == "ucs"):
    puzzle.ucs(cleaner_x, cleaner_y, horizontal_len)
elif(sys.argv[1] == "astar0"):
    print("only solved for uninformed, sorry")
#puzzle.ucs(cleaner_x, cleaner_y, horizontal_len)
#print(puzzle.the_path)
#GoalStates = findGoalStates(lines);


    
    