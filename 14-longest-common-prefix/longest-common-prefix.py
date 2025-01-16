class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if all(char == chars[0] for char in chars):
                prefix += chars[0]
            else: break
        return prefix