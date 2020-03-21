class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_len = 0
        longest_pal = ""
        slen = len(s)
        P = [[False for i in range(slen)] for j in range(slen)]
        for j in range(slen):
            P[j][j] = True
            if longest_len < 1:
                longest_len = 1
                longest_pal = s[j]
            for i in range(0, j):
                if s[i] == s[j] and j - i <= 2:
                    P[i][j] = True
                    if j - i + 1 > longest_len:
                        longest_len = j - i + 1
                        longest_pal = s[i:j+1]
                elif s[i] == s[j] and P[i+1][j-1]:
                    P[i][j] = True
                    if j - i + 1 > longest_len:
                        longest_len = j - i + 1
                        longest_pal = s[i:j+1]
        return longest_pal