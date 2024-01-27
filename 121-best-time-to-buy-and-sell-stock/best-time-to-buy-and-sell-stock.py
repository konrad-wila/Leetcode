class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # buy
        right = 1 # sell
        max_profit = 0 # optimal trade

        while  right < len(prices):
            # Check if profitable transaction
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit




        