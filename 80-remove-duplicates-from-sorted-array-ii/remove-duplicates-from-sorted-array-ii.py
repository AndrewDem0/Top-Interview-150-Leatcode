class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        This code uses two pointers to save memory. The `i` pointer is used for traversing
        and detecting duplicates, while `counter` constructs the resulting list and keeps
        track of the number of valid elements. The search for duplicate elements starts
        at index 2 because, in any case, the first two numbers will satisfy the conditions.
        """
        counter = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[counter - 2]:
                nums[counter] = nums[i]
                counter += 1
        return counter
