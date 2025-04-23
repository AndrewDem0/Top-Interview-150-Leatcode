from collections import Counter

class Solution:
    def MakeHashMap(self, string):
        HashMap = {}
        for char in string:
            HashMap[char] = 1 + HashMap.get(char, 0)
        return HashMap

    def isAnagram(self, s: str, t: str) -> bool:
        return self.make_hash_map(s) == self.make_hash_map(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True