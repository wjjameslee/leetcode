class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        costs = []
        # Initialize costs matrix which has the minimized sum of all numbers in its path from 0,0 to cell i,j
        for i in range(m):
            cost_row = []
            for j in range(n):
                cost_row.append(0)
            costs.append(cost_row)
        
        costs[0][0] = grid[0][0]
        # Make sure the first row and first column pre-compute the sum so far of its path to avoid index issues
        for i in range(1, m):
            costs[i][0] = costs[i-1][0] + grid[i][0]
        for j in range(1, n):
            costs[0][j] = costs[0][j-1] + grid[0][j]
        # Bottom-up DP
        for i in range(1, m):
            for j in range(1, n):
                costs[i][j] = min(costs[i-1][j] + grid[i][j], costs[i][j-1] + grid[i][j])
        return costs[m-1][n-1]