import copy
import heapq
from collections import namedtuple

class Solution:
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        def isGoalState(g, b):
            r = len(b)
            c = len(b[0])
            for i in range(r):
                for j in range(c):
                    if g[b[i][j]] != (i, j):
                        return False
            return True
        
        def calcHeuristic(goal_state, board):
            ret = 0
            r = len(board)
            c = len(board[0])
            for i in range(r):
                for j in range(c):
                    ret += abs(goal_state[board[i][j]][0] - i) + abs(goal_state[board[i][j]][1] - j)
            return ret

        def mnPuzzle(board):
            r = len(board)
            c = len(board[0])
            
            goal_state = {}
            # Initialize goal_state dictionary with board indices (0 is last)
            for i in range(r):
                for j in range(c):
                    if r*c == c*i + j + 1:
                        goal_state[0] = (i, j)
                        continue
                    goal_state[c*i + j + 1] = (i, j)
            State = namedtuple('State', ['total_cost', 'distance', 'board'])
            heap = [State(0, 0, board)]
            closed = []
            
            while len(heap):
                #print('iteration')
                state = heapq.heappop(heap)
                #print(state)
                if isGoalState(goal_state, state.board):
                    return state.distance
                else:
                    neighbours = []
                    # Find indices where '0' is
                    start = None
                    for i in range(r):
                        for j in range(c):
                            if state.board[i][j] == 0:
                                start = (i, j)
                    for offr, offc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        if 0 <= start[0] + offr < r and 0 <= start[1] + offc < c:
                            n_board = copy.deepcopy(state.board)
                            n_board[start[0]+offr][start[1]+offc], n_board[start[0]][start[1]] = n_board[start[0]][start[1]], n_board[start[0]+offr][start[1]+offc]
                            #print("Generated neighbour: ", n_board)
                            neighbours.append(n_board)
                    for neighbour in neighbours:
                        if neighbour in closed:
                            continue
                        heapq.heappush(heap, State(state.distance + 1 + calcHeuristic(goal_state, neighbour), state.distance + 1, neighbour))
                        #print(neighbour)
                        #print(state.distance+1)
                        #print(calcHeuristic(goal_state, neighbour))
                        #print(state.distance+1+calcHeuristic(goal_state, neighbour))
                closed.append(state.board)
            return -1
    
        return mnPuzzle(board)
        
    