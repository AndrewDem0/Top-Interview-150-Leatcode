class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        The algorithm uses 3 pointers to traverse the string.
        First, it checks whether the string exists at all.
        The for loop compares whether an element of string `s` matches an element of string `t`.
        If a match is found, in the next iteration the next character of string `s` is compared.
        If the entire string `s` is traversed, it returns True; otherwise, False.

        The second version is a concise implementation of the first.

        Complexity: Time Complexity: O(n + m), Space Complexity: O(1)
        """
        
        if not s:
            return True
        index_s = 0
        for i in t:
            if s[index_s] == i:
                index_s += 1
            if index_s == len(s):
                return True
        return False


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s = 0
        for i in t:
            if index_s < len(s) and s[index_s] == i:
                index_s += 1
        return index_s == len(s)
