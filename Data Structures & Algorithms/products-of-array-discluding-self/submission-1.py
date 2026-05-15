class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []

        for i in range(len(nums)):
            b = 1

            for j in range(len(nums)):
                if i != j:
                    b *= nums[j]

            a.append(b)

        return a