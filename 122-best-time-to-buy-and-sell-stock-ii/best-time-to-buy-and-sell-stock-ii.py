class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        
        max_profit = 0
        i = 0

        while i < len(prices) - 1:
            # Find the next local minimum
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = prices[i]

            # Find the next local maximum
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            sell = prices[i]

            max_profit += sell - buy

        return max_profit
        