"""
в першому варіант спочатку створюється новий рядок вже очищений від посторонніх символів
та записанийу нижньому регістрі після чого йде порівняння на полідром і видається відповідь

Time complexity: O(n) Space complexity: O(n)

другий алгоритм використовує два вказівники для преміщення по рядку і одночасно фільтрує
його елементи, не створюючи нового рядка.

Time complexity: O(n) Space complexity: O(1)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual_s =''.join(filter(str.isalnum, s)).lower()

        if actual_s != actual_s[::-1]: 
            return False
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
                
        return True
