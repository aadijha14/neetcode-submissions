class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # s = set()
        # for i in nums:
        #     s.add(i)
        s = set(nums)
        if len(s) != len(nums):
            return True
        else:
            return False