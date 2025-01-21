class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual_s =''.join(filter(str.isalnum, s)).lower()

        if actual_s != actual_s[::-1]: return False
        return True