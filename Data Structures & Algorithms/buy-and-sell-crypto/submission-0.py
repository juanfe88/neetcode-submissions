class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float("inf")
        sell = float("-inf")
        for price in prices:
            if price < buy:
                buy = price
                sell = 0
                continue
            if price > sell:
                sell = price
                profit = sell - buy
                max_profit = max(max_profit, profit)
        return max_profit
