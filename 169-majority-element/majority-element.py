class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {} #use dictionary to track how many times does each number appear
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for key, times in dict.items():
            if times >= len(nums) / 2:
                return key