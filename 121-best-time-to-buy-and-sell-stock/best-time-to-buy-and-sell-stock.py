class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This approach uses two pointers and a variable to track the maximum profit.
        It is implemented using a while loop that iterates through all values in the array.
        If the buying price is greater than the selling price, the buy pointer moves to the smaller
        price.
        If the prices are in correct order (buy price is less than sell price), the
        'profit' variable stores the largest difference found.
        max_number = max(number1, number2) selects the larger value and stores it in the
        'profit' variable.
        After that, the selling pointer moves forward by 1 position.
        Since max cannot return a negative value, there's no need to perform an extra check
        for negative profit.

        Video explanation: https://youtu.be/yILVtZd-VkY

        The reference solution is provided below.

        Both methods have: Time complexity: O(n) Space complexity: O(1)
        """
        
        profit = 0
        buy_index = 0
        sell_index = 1
        while sell_index < len(prices):
            if prices[buy_index] > prices[sell_index]:
                buy_index = sell_index
            else:
                profit = max(profit, prices[sell_index] - prices[buy_index])
                sell_index += 1
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = float('inf')  # The minimum price encountered so far
        profit = -float('inf')  # The maximum profit encountered so far

        for price in prices:
            m = min(price, m)  # Update the minimum price
            profit = max(price - m, profit)  # Calculate profit and update the maximum profit
        
        return profit