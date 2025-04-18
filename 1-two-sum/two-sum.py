class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search_pointer = 1
        base_pointer = 0
        while (base_pointer < len(nums)):
            if nums[search_pointer] + nums[base_pointer] == target:
                return [search_pointer, base_pointer]
            else:
                if search_pointer < len(nums) - 1:
                    search_pointer += 1
                else:
                    base_pointer += 1
                    search_pointer = base_pointer + 1
        return False
        