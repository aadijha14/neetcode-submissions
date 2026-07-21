class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            prod = 1
            for j in range(0, i):
                prod *= nums[j]
            for j in range(i+1, len(nums)):
                prod *= nums[j]
            result.append(prod)
        
        return result

