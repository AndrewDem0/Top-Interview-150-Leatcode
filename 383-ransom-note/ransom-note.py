class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_h = {}

        for c in magazine:
            mag_h[c] = 1 + mag_h.get(c,0)

        for c in ransomNote:
            if  c not in mag_h or mag_h[c] <= 0:
                return False
            mag_h[c] -= 1
        return True