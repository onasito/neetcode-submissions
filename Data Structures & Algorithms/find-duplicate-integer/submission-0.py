class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # second phase
        slow2 = 0
        while nums[slow2] != nums[slow]:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return nums[slow]