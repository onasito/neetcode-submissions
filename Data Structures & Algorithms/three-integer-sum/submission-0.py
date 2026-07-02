class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate i
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                ans = nums[i] + nums[left] + nums[right]

                if ans == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:  # skip duplicate left
                        left += 1
                    while left < right and nums[right] == nums[right+1]:  # skip duplicate right
                        right -= 1
                
                elif ans < 0:
                    left += 1
                
                elif ans > 0:
                    right -= 1

        return result
            
            