class Solution:
    def climbStairs(self, n: int) -> int:
        numSteps = [1, 2]
        for i in range(2,n):
            numSteps.append(numSteps[i-2] + numSteps[i-1])
        return numSteps[n-1]
            