class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        L = len(s)
        mid = (L // 2)
        for i in range(mid):
            s[i], s[L-i-1] = s[L-i-1], s[i]
        return s