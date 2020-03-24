class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurrences = {}
        for c in s:
            if c not in occurrences:
                occurrences[c] = 1
            else:
                occurrences[c] += 1
        L = len(s)
        for i in range(L):
            if occurrences[s[i]] == 1:
                return i
        return -1