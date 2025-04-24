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

class Solution:
    def isHappy(self, n: int) -> bool:
        
        rec = []

        while n != 1:
            n_s = str(n)
            n = 0

            for x in n_s:
                n += pow(int(x),2)

            if n in rec:
                return False
            
            rec.append(n)        

        return True
