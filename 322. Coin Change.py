class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = math.inf
        # dp[i] is the # of coins (fewest) to make up total sum, i
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        if math.isinf(dp[-1]):
            return -1
        return dp[-1]
        