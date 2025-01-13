class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        сенс полягає в тому щоб продавати акції як тільки знайдеться варіант з прибутком 
        використаний елементарний спосіб порівнняння найближчих значень масиву, далі відбувається
        вирахування профіту і значення всих вдалих операціцй повертається.

        Complexity: Time complexity: O(n), Space complexity: O(1)

        посилання на роз'яснення: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solutions/5816678/video-sell-a-stock-immediately
        """
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit