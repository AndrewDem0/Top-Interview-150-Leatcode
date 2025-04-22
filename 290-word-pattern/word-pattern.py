class Solution:
    def dupl(self, dict):
        return len(set(dict.values())) < len(dict.values())

    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(pattern) < len(s_list):
            return False
        index = 0
        h_map = {}
        for char in pattern:
            if char not in h_map:
                h_map[char] = s_list[index]
            if h_map[char] != s_list[index] or self.dupl(h_map) == True:
                return False
            if len(s_list) > 1:
                index += 1
        return True