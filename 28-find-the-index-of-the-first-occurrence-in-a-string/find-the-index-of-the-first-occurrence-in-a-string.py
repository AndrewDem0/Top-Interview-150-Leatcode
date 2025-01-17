class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        цей алгоритм проходить весь рядок haystack і шукає на проміжку довжиною
        шуканого слова це слово, якщо не знаходить його то пересувається на 1 
        індекс вперед поки не пройде весь рядок.

        Time Complexity = O(n * m) Space Complexity = O(1)
        """
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1