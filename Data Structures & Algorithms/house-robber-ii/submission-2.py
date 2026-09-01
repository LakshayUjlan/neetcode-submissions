class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def rob1(arr):
            if len(arr) == 1:
                return arr[0]
            n=len(arr)
            dp = [0]*n 
            dp[0] = arr[0]
            dp[1] = max(arr[0] , arr[1])
            for i in range(2,n):
                dp[i] = max(arr[i]+dp[i-2] , dp[i-1])
            return dp[-1]
        return  max(rob1(nums[1:]),rob1(nums[:-1]))