class Solution:
    def checkRecord(self, s: str) -> bool:
        occurrences = {'A': 0, 'L': 0, 'P': 0}
        for c in s:
            if c in occurrences:
                occurrences[c] += 1
        maxcons = 0
        cons = 0
        for c in s:
            if c == 'L':
                cons += 1
            else:
                maxcons = max(maxcons, cons)
                cons = 0
        maxcons = max(maxcons, cons)
        if occurrences['A'] > 1:
            return False
        if maxcons > 2:
            return False
        return True