class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        This algorithm uses 3 pointers: `i` - the start, `k` - the end of the array, 
        and between them the pointer `j` moves. The `i` pointer is updated 
        using a for loop, which is also responsible for restarting the iteration
        through the array. Before starting the iterations, the array is sorted
        for more convenient exploration. The `k` pointer is moved to decrease the largest
        number among the considered elements for proper comparison, and the `j` pointer
        iterates over the potential numbers that can act as the middle element of the desired
        triplet.Additionally, checks are performed for `i` and `j` to prevent duplicates
        in the result when there are two identical values in the array.

        Time complexity: O(n*n) Space complexity: O(n)
        """

        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res
