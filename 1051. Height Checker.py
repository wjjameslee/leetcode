class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        minimum, maximum = min(heights), max(heights)
        values = {i: 0 for i in range(minimum, maximum+ 1)}
        comp = []
        for elem in heights:
            values[elem] += 1
        for k, v in values.items():
            comp += [k] * v
        print(comp)
        L = len(heights)
        num_moves = 0
        for i in range(L):
            if comp[i] != heights[i]:
                num_moves += 1
        return num_moves