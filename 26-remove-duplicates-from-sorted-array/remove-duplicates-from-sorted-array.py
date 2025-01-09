class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[counter] = nums[i]
                counter += 1
        return counter
"""
This code uses the two-pointer technique and checks by comparing the current element in the
array with the previous index. "The current element is compared with the previous one to 
find unique elements and avoid going out of bounds of the list. Additionally, the iteration
starts from the element at index 1 to prevent an error caused by checking values outside
the array.
"""
