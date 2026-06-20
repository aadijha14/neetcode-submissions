class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            if nums[i] in dict1.keys():
                dict1[nums[i]].append(i)
            else:
                dict1[nums[i]] = [i]
        
        keys = dict1.keys()
        for i in keys:
            index = dict1[i].pop(0)
            find = target - i
            if find in keys and len(dict1[find]) > 0:
                return [index, dict1[find].pop(0)]