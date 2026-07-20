class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        min_val = nums[0]

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] >= nums[high]:
                min_val = min(min_val, nums[mid])
                low = mid+1
            elif nums[mid] < nums[high]:
                min_val = min(min_val, nums[mid])
                high = mid-1
        
        return min_val