class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a={}
        b=[]
        for x in nums:
            if x in a:
                a[x]+=1
            else:
                a[x]=1
        for key,val in a.items():
            if val>len(nums)/3:
                b.append(key)
        return b