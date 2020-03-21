class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max(prices[i] - cheapest[i]
        cheapest = []
        plen = len(prices)
        
        smallSoFar = 0
        for i in range(plen):
            if i == 0:
                smallSoFar = prices[i]
                cheapest.append(smallSoFar)
                continue
            if prices[i] < smallSoFar:
                smallSoFar = prices[i]
            cheapest.append(smallSoFar)
        
        max_profit = 0
        for i in range(1, plen):
            profit = prices[i] - cheapest[i-1]
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
                