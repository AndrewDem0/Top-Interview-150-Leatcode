class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}
        for inx, num in enumerate(nums):
            if num in h_map and inx - h_map[num] <= k:
                return True
            h_map[num] = inx
        return False
