class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
            
        max_profit = prices[1] - prices[0] 
        min_price = prices[0]

        for idx in range(1, len(prices)):
            if prices[idx] - min_price > max_profit:
                max_profit = prices[idx] - min_price
            if prices[idx] < min_price:
                min_price = prices[idx]
            if max_profit < 0:
                max_profit = 0
        return max_profit
