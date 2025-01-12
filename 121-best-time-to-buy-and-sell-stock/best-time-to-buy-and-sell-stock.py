class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        buy_index = 0
        sell_index = 1
        while sell_index < len(prices):
            if prices[buy_index] > prices[sell_index] :
                buy_index = sell_index

            profit = max(profit, prices[sell_index] - prices[buy_index])
            sell_index += 1
            
        return profit