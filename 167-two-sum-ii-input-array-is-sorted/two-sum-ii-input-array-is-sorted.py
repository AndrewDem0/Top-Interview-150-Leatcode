class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        This method uses the two-pointer approach to find the result. If the sum of two numbers
        is greater than the target, the right pointer moves to the left. If the sum is smaller,
        the left pointer moves to the right. In case of the correct answer, the values 
        are returned.

        Link to the solution: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solutions/5101915/video-using-two-pointers-to-solve-the-question-with-o-1-space

        Time complexity: O(n) Space complexity: O(1)
        """

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
        return False
