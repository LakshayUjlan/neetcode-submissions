class Solution:
    def lastStoneWeight(self, nums: List[int]) -> int:
        nums = [-x for x in nums]
        heapq.heapify(nums)
        while len(nums)>1:
            
            
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            if first != second:
                heapq.heappush(nums,first-second)
        if nums:
            return -nums[0]
        return 0
        
        