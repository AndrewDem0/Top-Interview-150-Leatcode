class Solution:
    def maxArea(self, height: List[int]) -> int:
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
