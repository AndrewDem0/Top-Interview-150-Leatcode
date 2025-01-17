class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        The algorithm uses zip to break each word in the array into tuples of letters
        at the same index. If the letters match, they are added to the `prefix` variable.
        If a mismatch occurs, the loop stops. Finally, the `prefix` variable is returned.

        Time Complexity = O(n * m), where n is the number of strings and m is the average 
        length of the strings.
        Space Complexity = O(n + m), due to the storage of zipped characters and the prefix.

        The second approach takes the entire first word as the prefix and compares it with
        the other words.
        If no match is found, the first word in the array is shortened by one letter at a time
        until either the whole word is checked or a common prefix is found. Finally, the `prefix`
        is returned.

        Time Complexity = O(S), where S is the total number of characters in all strings.
        Space Complexity = O(m), where m is the length of the first word (since only the prefix
        is stored).
        """

        prefix = ""
        for chars in zip(*strs):
            if all(char == chars[0] for char in chars):
                prefix += chars[0]
            else:
                break
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        for i in range(1, len(strs)):
            # Compare the current string with the prefix
            while strs[i][: len(prefix)] != prefix:
                # Reduce the prefix length until it matches
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
