class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        n=len(nums)
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        b=[]
        for key in sorted(freq, key=freq.get, reverse=True)[:k]:
            b.append(key)
        return b


