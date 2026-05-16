class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans_arr = [0] * n
        
        # Count zeros and calculate the product of non-zero elements
        zero_count = nums.count(0)
        if zero_count > 1:
            return ans_arr  # More than one zero means all products are zero
        
        total_mult = 1
        for num in nums:
            if num != 0:
                total_mult *= num
        
        # Fill the answer array based on the zero count
        for i in range(n):
            if zero_count == 0:
                ans_arr[i] = total_mult // nums[i]
            elif nums[i] == 0:
                ans_arr[i] = total_mult  # Only the position with zero gets the product of non-zero elements
        
        return ans_arr