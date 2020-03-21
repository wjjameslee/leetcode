class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        alen = len(A)
        a = A
        iterations = 10000 // alen
        for i in range(iterations):
            if B in a:
                return i + 1
            a += A
        if B in a:
            return iterations
        return -1