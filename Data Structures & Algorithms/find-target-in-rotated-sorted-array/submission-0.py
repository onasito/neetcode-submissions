class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                return mid

            # left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:  # target in left half
                    high = mid - 1
                else:  # target in right half
                    low = mid + 1
            # right half is sorted
            else:
                if nums[mid] < target <= nums[high]:  # target in right half
                    low = mid + 1
                else:  # target in left half
                    high = mid - 1

        return -1