class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        c=[]
        cursum = 0
        for b in range(len(nums)-2):
            if b > 0 and nums[b] == nums[b - 1]:
                continue
            left = b + 1
            right = len(nums) - 1
            while left<right:
                cursum = nums[left] + nums[right] +nums[b]
                if  cursum == 0 :
                    c.append([nums[b],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif (cursum) < 0 :
                    left+=1
                else:
                    right-=1
        return c
            
                
