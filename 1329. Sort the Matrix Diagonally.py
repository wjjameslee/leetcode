class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        start_positions = [(0, c) for c in range(n)]
        start_positions.extend([(r, 0) for r in range(1, m)])
        
        for r, c in start_positions:
            i, j = r, c
            diagonal = []
            
            while i < m and j < n:
                diagonal.append(mat[i][j])
                i += 1
                j += 1
            diagonal.sort()
            
            i, j = r, c
            idx = 0
            while i < m and j < n:
                mat[i][j] = diagonal[idx]
                i += 1
                j += 1
                idx +=1
        
        return mat
