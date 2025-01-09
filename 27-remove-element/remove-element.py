class Solution:
    def removeElement(self, nums: List[int], val: int) -> int: 
        """ 
        This task uses two pointers to traverse the array:
        i is used to check the value of each element to satisfy the condition,
        and counter is used to track the position where the element that satisfies the condition should be moved.
        Since the task does not require preserving the elements that do not meet the condition, they can be replace
        """
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums [i]
                counter += 1
        return counter
