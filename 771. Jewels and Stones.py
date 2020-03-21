class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num_jewels = 0
        jewels = set(J)
        return sum(stone in jewels for stone in S)