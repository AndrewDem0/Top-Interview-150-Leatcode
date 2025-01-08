class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Create pointers for each array to traverse through the arrays
        pointer_m = m - 1 
        pointer_n = n - 1
        pointer_solution = m + n - 1

        """
        The loop runs until all elements of nums2 are processed.
        The first "if" handles cases where nums1 has not been fully traversed from the end,
        and the current number in nums1 is greater than the current number in nums2. 
        In this case, the value from nums1 remains unchanged and the nums1 pointer 
        moves one step forward.
        If the compared number in nums2 is greater than nums1, it is written 
        at the position of the overall pointer, and the nums2 pointer moves to the next element.
        After the final iteration, the overall pointer moves one position back 
        for the next iteration.
        """
        while pointer_n >= 0: 
            if pointer_m >= 0 and nums1[pointer_m] > nums2[pointer_n]:
                nums1[pointer_solution] = nums1[pointer_m]
                pointer_m -= 1
            else:
                nums1[pointer_solution] = nums2[pointer_n]
                pointer_n -= 1
            
            pointer_solution -= 1
