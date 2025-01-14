class Solution:
    def romanToInt(self, s: str) -> int:
        """
        This solution uses a dictionary to map Roman numeral symbols to their integer values.
        The `zip` function is used to pair the current character with the next one by slicing
        the string. This creates a sliding window of pairs for comparison. The loop could
        also be written as:

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]

        The comparison logic subtracts the value of the current character if the next one is
        greater; otherwise, it adds the current value. Since the last character has no pair,
        its value is added to the result after the loop.

        Complexity: Time complexity: O(n) Space complexity: O(1)
        """
        
        ans = 0
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for a, b in zip(s, s[1:]):
            if table[a] < table[b]:
                ans -= table[a]
            else:
                ans += table[a]
        return ans + table[s[-1]]
