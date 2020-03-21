class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s, letters_t = {}, {}
        for c in s:
            if c not in letters_s:
                letters_s[c] = 1
            else:
                letters_s[c] += 1
        for c in t:
            if c not in letters_t:
                letters_t[c] = 1
            else:
                letters_t[c] += 1
        if letters_s != letters_t:
            return False
        return True
        