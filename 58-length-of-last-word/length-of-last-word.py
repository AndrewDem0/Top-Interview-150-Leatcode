class Solution:
    """
    My method uses primitive constructs, specifically creating a variable to count letters.
    It iterates through the string from the end to the beginning. If it encounters a letter,
    it increments the counter. If it encounters a space, the loop stops and returns the count.
    In cases where there are trailing spaces at the end, the loop continues because of the
    condition that checks if the counting has already started.

    Complexity: Time complexity: O(n), Space complexity: O(1)

    The second method first removes all extra spaces (at the beginning and end, until a word
    appears) using `strip()`. Then, it splits the string into a list of words, separating them
    by spaces, and returns the length of the last word. Since the `split` method creates a new
    list, this approach uses more memory.

    Complexity: Time complexity: O(n), Space complexity: O(n)
    """

    def lengthOfLastWord(self, s: str) -> int:
        lenght = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i].isalpha():
                lenght += 1
                print(lenght)
            elif s[i].isspace() and lenght != 0:
                return lenght
        return lenght


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split(" ")
        return len((s[-1]))
