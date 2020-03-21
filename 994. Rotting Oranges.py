class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        row = len(grid)
        col = len(grid[0])
        visited = [[False for j in range(col)] for i in range(row)]
        stack, apply_change = [], []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    stack.append((i, j, 0))

        while len(stack) != 0:
            rotten = stack.pop(0)     
            if rotten[0] < 0 or rotten[0] == row or rotten[1] < 0 or rotten[1] == col or grid[rotten[0]][rotten[1]] == 0 or visited[rotten[0]][rotten[1]]:
                continue
            visited[rotten[0]][rotten[1]] = True
            if grid[rotten[0]][rotten[1]] == 1:
                apply_change.append(rotten)
            stack.append((rotten[0]-1, rotten[1], rotten[2]+1)) # North
            stack.append((rotten[0], rotten[1]-1, rotten[2]+1)) # East
            stack.append((rotten[0]+1, rotten[1], rotten[2]+1)) # South
            stack.append((rotten[0], rotten[1]+1, rotten[2]+1)) # South
        for coord in apply_change:
            grid[coord[0]][coord[1]] = 2
        
        print(grid)
        for i in range(row):
            for j in range(col):
                 if grid[i][j] == 1:
                        return -1
        return 0 if len(apply_change) == 0 else apply_change[-1][2]