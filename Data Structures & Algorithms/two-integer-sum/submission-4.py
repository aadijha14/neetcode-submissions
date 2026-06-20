class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_test = nums.copy()
        while len(nums_test) > 0:
            num = nums_test.pop(0)
            find = target - num
            if find in nums_test and find != num:
                return [nums.index(num), nums.index(find)]
            elif find in nums_test and find == num:
                num_index = nums.index(num)
                nums[nums.index(num)] = 99999999 #INT_MAX
                find_index = nums.index(num)
                return [num_index, find_index]


            