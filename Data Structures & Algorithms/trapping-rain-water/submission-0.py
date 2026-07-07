class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        max_pre, max_suf = 0, 0

        for i in range(len(height)):
            max_pre = max(max_pre, height[i])
            prefix.append(max_pre)

        for i in range(len(height) - 1, -1, -1):
            max_suf = max(max_suf, height[i])
            suffix.append(max_suf)

        suffix = suffix[::-1]

        water = 0
        for i in range(len(height)):
            water += min(prefix[i], suffix[i]) - height[i]

        return water