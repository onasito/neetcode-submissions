class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        deque = collections.deque()  # stores indices
        left, right = 0, 0

        while right < len(nums):
            # remove smaller values from the back
            while deque and nums[deque[-1]] < nums[right]:
                deque.pop()
            deque.append(right)

            # remove left element if it's out of window
            if deque[0] < left:
                deque.popleft()

            # add to result once window is full
            if right + 1 >= k:
                result.append(nums[deque[0]])
                left += 1

            right += 1

        return result