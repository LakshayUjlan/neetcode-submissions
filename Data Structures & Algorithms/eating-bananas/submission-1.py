import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans=right
        while left<=right:
            t=0
            k = (left+right)//2
            for i in range(0,len(piles)):
                t += math.ceil(piles[i]/k)
            if t>h:
                left = k+1
            else:
                ans=k
                right=k-1
        return ans
        