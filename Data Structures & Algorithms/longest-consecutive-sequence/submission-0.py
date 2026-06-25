class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_seq = 0

        for num in my_set:
            if num - 1 not in my_set:
                count = 1
                i = 1
                while num + i in my_set:
                    count +=1
                    i+=1
                max_seq = max(max_seq, count)

        return max_seq