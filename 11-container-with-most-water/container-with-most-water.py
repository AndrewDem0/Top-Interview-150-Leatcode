class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The algorithm uses two pointers: the left pointer starts at the beginning of 
        the array, and the right pointer starts at the end of the array.
        The built-in `min` function is used to find the smaller of the two columns to
        determine the x-coordinate,
        while the y-value is calculated as the difference between the pointers.
        The built-in `max` function is then applied to store the largest area found so far.
        The result is returned at the end. The pointers move by one position
        based on the following rule:
        the pointer corresponding to the smaller value moves.

        Time complexity: O(n) Space complexity: O(1)
        """

        left_p = 0
        right_p = len(height) - 1
        champ = 0

        while left_p < right_p:
            x = right_p - left_p
            y = min(height[left_p], height[right_p])
            candidate = x * y
            champ = max(champ, candidate)
            if height[left_p] <= height[right_p]:
                left_p += 1
            else:
                right_p -= 1
        return champ
