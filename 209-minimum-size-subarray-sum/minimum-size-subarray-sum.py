class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        цей алгоритм побудований на принципі ковзаючого вікна, це дозволяє обраховувати
        меншу кількість елементів ніж грубим методом, а саме існують 2 вказівники, що
        пересуваються по масиву, кол сума членів масиву між цими вказівниками >= target
        значеня порівнюється за допомогою min(), після цього віднімається кільксть елементів
        з ліва так щоб вийшло що сума менше target після цього додаються елементи за 
        допомогою вказівника right, в кінці повернеться значення найменшого рядка, або
        якщо не вистачить суми елементів щоб досягти target то 0.

        Time complexity: O(n) Space complexity: O(1)
        """
        min_len = float("inf")
        left = 0
        cur_sum = 0
        
        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return min_len if min_len != float("inf") else 0