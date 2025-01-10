class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        This problem uses the Boyer-Moore algorithm, which finds a candidate
        for the element that appears more than n/2 times. Each time the counter reaches
        zero, a new candidate is selected for verification.
        The algorithm works only when there is a single dominant value.
        """
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate
