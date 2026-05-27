class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq={}
        for a in nums:
            if a in freq:
                freq[a]+=1
            else:
                freq[a]=1
            if freq[a]>1:
                return a