class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        n=len(nums)
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
            if freq[x]>n//2:
                return x