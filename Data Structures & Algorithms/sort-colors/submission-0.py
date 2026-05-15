class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        for i in range(0,len(nums)):
            mini=i
            for j in range(i+1,len(nums)):
                if(nums[j]<nums[mini]):
                    mini=j
            nums[i] , nums[mini] = nums[mini] , nums[i]

                    
    

        