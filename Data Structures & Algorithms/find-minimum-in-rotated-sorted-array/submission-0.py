class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        for a in nums:
            if a<mini:
                mini=a
        return mini