class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s,t))) 

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_m = {} 
        for sc, tc in zip(s,t):
            if sc in char_m:
                if char_m[sc] != tc:
                    return False
            elif tc in char_m.values():
                return False
            
            char_m[sc] = tc
        
        return True

