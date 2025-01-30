class Solution:
    def duplicate(self, s, left, right):
        seen = set()
        for char in s[left:right + 1]:
            if char in seen:
                return True
            else:
                seen.add(char)
        return False



    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        if len(s) == 1:
            return 1
        if not s:
            return 0
        while right < len(s):

            if self.duplicate(s, left, right) == True:
                left += 1
            else: 
                right +=1
                
            max_len = max(max_len, right - left)
        return max_len
