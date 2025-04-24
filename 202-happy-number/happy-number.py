class Solution:
    def Check (self, n: int):
        count  = 0
        while n:
            digit = n % 10
            count += pow(digit, 2)
            n //= 10
        return count

    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.Check(n)
            if n == 1:
                return True
        return False