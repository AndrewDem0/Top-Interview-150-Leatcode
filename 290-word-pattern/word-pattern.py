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

def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for c, w in zip(pattern, words):
        if c in char_to_word:
            if char_to_word[c] != w:
                return False
        else:
            if w in word_to_char:
                return False
            char_to_word[c] = w
            word_to_char[w] = c

    return True
