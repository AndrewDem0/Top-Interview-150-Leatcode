class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        This method is one of the simplest for this problem. It focuses on the idea that
        we do not need to always use the full value of the array element. This prevents issues 
        in situations like [2,5,0,0]. The main principle is the simulation of a gas station, 
        and during the traversal, the "gas" is optimally refueled, rather than just using the 
        value that appears. 
        If we can reach the end of the array, we return True; otherwise, when the fuel runs out 
        earlier, we return False.

        Complexity: Time complexity: O(n) Space complexity: O(1)

        Reference to the original solution: https://leetcode.com/problems/jump-game/solutions/4534808/super-simple-intuitive-8-line-python-solution-beats-99-92-of-users
        """
        gas = 0
        for i in nums:
            if gas < 0: return False
            elif i > gas: gas = i
            gas -= 1
        return True
