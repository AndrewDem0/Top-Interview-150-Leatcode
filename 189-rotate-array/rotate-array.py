class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        This solution uses the slicing method `nums[start:stop:step]`. 
        Before rotating, we calculate the remainder `%` of `k` divided by the length of the array 
        to avoid unnecessary rotations.

        The `-k` is used to work with the array starting from the end. 
        If `k` is used directly, the rotation would happen to the left instead of the right. 

        The first slice (`nums[-k:]`) takes the last `k` elements of the array, 
        and the second slice (`nums[:-k]`) takes the elements from the start up to `len(nums) - k`. 
        These slices are combined using the `+` operator to form the rotated array.

        Using `nums[:]` ensures that we modify the original array in-place instead of creating a
        new one.

        Time Complexity: O(n), Space Complexity: O(n)

        Below is a reference solution that uses an in-place permutation method, 
        implemented manually by reversing sections of the array. The reversal is performed in 
        three steps: reverse the entire array, reverse the first `k` elements, and reverse the rest.

        Time Complexity: O(n), Space Complexity: O(1)

        Credit: https://leetcode.com/u/bloomh/
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(start, end):  # Helper method to reverse elements between start and end
            while start < end:  # Continue until pointers meet
                nums[start], nums[end] = nums[end], nums[start]  # Swap elements
                start, end = start + 1, end - 1  # Move pointers inward
        
        n = len(nums)
        k %= n  # Adjust k for cases where k > len(nums)
        reverse(0, n - 1)  # Reverse the entire array
        reverse(0, k - 1)  # Reverse the first k elements (which were originally the last k)
        reverse(k, n - 1)  # Reverse the remaining elements