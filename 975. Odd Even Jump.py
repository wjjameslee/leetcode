class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        
        def find_jumps(idx_arr):
            l = len(idx_arr)
            ret = [None] * l
            stack = []
            for idx in idx_arr:
                while stack and idx > stack[-1]:
                    ret[stack.pop()] = idx
                stack.append(idx)
            return ret
        
        N = len(A)
        oddjumps = find_jumps(sorted(range(N), key = lambda i: A[i]))
        evenjumps = find_jumps(sorted(range(N), key = lambda i: -A[i]))
        oddstart = [False] * N
        evenstart = [False] * N
        oddstart[N-1], evenstart[N-1] = True, True
        
        for i in range(N-2, -1, -1):
            if oddjumps[i] is not None:
                oddstart[i] = evenstart[oddjumps[i]]
            if evenjumps[i] is not None:
                evenstart[i] = oddstart[evenjumps[i]]
        
        return sum(oddstart)
