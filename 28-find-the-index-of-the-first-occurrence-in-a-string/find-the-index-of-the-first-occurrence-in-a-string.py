class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        This algorithm traverses the string `haystack` and checks a substring 
        of the same length as the `needle`. If it doesn't find the `needle`, 
        it shifts one index forward until it traverses the entire string.

        Time Complexity = O(n * m), Space Complexity = O(1)
        """
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1