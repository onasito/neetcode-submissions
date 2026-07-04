class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        i,j = 0,0
        counter = 0
        longest_string= 0
        while j < len(s):
            if s[j] in seen:
                seen.discard(s[i])
                i+=1
                counter-=1
            else:
                seen.add(s[j])
                j+=1
                counter+=1
                longest_string = max(longest_string, counter)
        return longest_string