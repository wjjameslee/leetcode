class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        from collections import deque
        to_change = []
        stack = deque()
        
        # Initialize visted list which keeps track of already visited pixels
        visited = []
        num_rows = len(image)
        num_cols = len(image[0])
        for i in range(num_rows):
            row = []
            for j in range(num_cols):
                row.append(False)
            visited.append(row)
        
        to_change.append((sr, sc))
        stack.append((sr, sc))
        while len(stack) != 0:
            new_pixel = stack.pop()
            if new_pixel[0] < 0 or new_pixel[1] < 0 or new_pixel[0] == num_rows or new_pixel[1] == num_cols or visited[new_pixel[0]][new_pixel[1]]:
                continue
            
            visited[new_pixel[0]][new_pixel[1]] = True
            if image[new_pixel[0]][new_pixel[1]] == image[sr][sc]:
                to_change.append((new_pixel[0], new_pixel[1]))
                stack.append((new_pixel[0] - 1, new_pixel[1]))
                stack.append((new_pixel[0] + 1, new_pixel[1]))
                stack.append((new_pixel[0], new_pixel[1] - 1))
                stack.append((new_pixel[0], new_pixel[1] + 1))
        
        for affected in to_change:
            image[affected[0]][affected[1]] = newColor
        return image