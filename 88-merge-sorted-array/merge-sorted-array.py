class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer_m = m-1
        pointer_n = n-1
        pointer_solution = m+n-1

        while (pointer_n >=0):
            if pointer_m >= 0 and nums1[pointer_m] > nums2[pointer_n]:
                nums1[pointer_solution] = nums1[pointer_m]
                pointer_m -= 1
            else:
                nums1[pointer_solution] = nums2[pointer_n]
                pointer_n -=1
            
            pointer_solution -=1