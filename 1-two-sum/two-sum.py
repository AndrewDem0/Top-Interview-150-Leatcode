class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ValMap = {}
        for index, num in enumerate(nums):
            search = target - num
            if search in ValMap:
                return [ValMap[search], index]
            ValMap[num] = index
