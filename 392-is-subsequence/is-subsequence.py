class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index_s = 0
        for i in t:
            if s[index_s] == i:
                index_s += 1
            if index_s == len(s):
                return True
        return False