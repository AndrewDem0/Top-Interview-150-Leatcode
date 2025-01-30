class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This algorithm uses the sliding window technique. As the `right` pointer moves
        through the array, it adds each encountered character to the `char_set`.

        If, during an iteration, we encounter a character that is already in `char_set`,
        we remove characters from the set that the `left` pointer is pointing to, moving `left`
        forward until the duplicate character is removed.

        When `right` encounters a new character, it adds it to `char_set` and updates
        `max_len`, comparing it to the longest sequence found so far.

        Time complexity: O(n) Space complexity: O(1)
        """

        max_len = 0
        left = 0
        char_set = set()

        for right in range(len(s)):

            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
