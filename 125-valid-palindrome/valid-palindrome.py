class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        actual_s =''.join(filter(str.isalnum, s))
        actual_s = actual_s.lower()

        for i in range(len(actual_s) // 2):
            if actual_s[i] != actual_s[-(i + 1)]:
                return False
        return True