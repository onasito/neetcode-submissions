class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_s = high

        while low <= high:
            mid = low + (high-low) // 2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            if hours <= h:
                result = mid
                min_s = min(min_s, mid)
                high = mid-1
            elif hours > h:
                low = mid+1
        
        return min_s