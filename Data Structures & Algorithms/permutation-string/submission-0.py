class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = [0]*26
        count2 = [0]*26
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')]+=1
        
        left = 0
        for right in range(len(s2)):
            count2[ord(s2[right]) - ord('a')]+=1

            if (right-left+1) > len(s1):
                count2[ord(s2[left]) - ord('a')]-=1
                left+=1

            if count2 == count1:
                return True
        
        return False