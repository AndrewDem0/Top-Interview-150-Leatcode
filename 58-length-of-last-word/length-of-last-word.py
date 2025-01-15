class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        for i in range(len(s) -1, -1, -1):
            if s[i].isalpha():
                lenght +=1
                print(lenght)
            elif (s[i].isspace() and lenght != 0):
                return lenght
        return lenght