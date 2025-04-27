class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        score = 1
        answ = []
        if not nums:
            return answ

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 != nums[i] and score == 1:
                answ.append(str(nums[i - 1]))
            elif score != 1 and nums[i - 1] + 1 != nums[i]:
                answ.append(f"{nums[i - score]}->{nums[i - 1]}")
                score = 1
            else:
                score += 1
            
        if score == 1:
            answ.append(str(nums[-1]))
        else:
            answ.append(f"{nums[len(nums) - score]}->{nums[- 1]}")
        return answ