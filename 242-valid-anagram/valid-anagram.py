class Solution:
    def MakeHashMap(self, string):
        HashMap = {}
        for char in string:
            HashMap[char] = 1 + HashMap.get(char, 0)
        return HashMap

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Hash_s = self.MakeHashMap(t)
        Hash_t = self.MakeHashMap(s)

        for i in Hash_s.keys():
            if i not in Hash_t.keys() or Hash_s[i] != Hash_t[i]:
                return False
        
        return True