class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1.keys():
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        
        ranking = sorted(dict1.items(), key = lambda pair: pair[1], reverse = True)

        result = []
        for i in range(k):
            result.append(ranking[i][0])
        
        return result
