class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h_map = {}
        for inx, num in enumerate(nums):
            if num in h_map and abs(h_map.get(num) - inx) <= k:
                return True
            h_map[num] = inx
        return False
