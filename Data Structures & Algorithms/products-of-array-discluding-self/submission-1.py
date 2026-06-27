class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        running = 1
        for i in range(len(nums)):
            prefix[i] = running
            running *= nums[i]

        running = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = running
            running *= nums[i]

        return [prefix[i] * suffix[i] for i in range(len(nums))]