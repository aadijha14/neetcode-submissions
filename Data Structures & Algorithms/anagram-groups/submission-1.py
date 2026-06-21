class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        
        for i in range(len(strs)):
            dict2 = {}
            for j in strs[i]:
                if j in dict2.keys():
                    dict2[j] += 1
                else:
                    dict2[j] = 1
            dict1[i] = dict2
        
        result = []
        indexes = []
        keys = list(dict1.keys())
        for i in range(len(keys)):
            if keys[i] in indexes:
                continue
            else:
                indexes.append(keys[i])
                temp = []
                temp.append(strs[keys[i]])

                for j in range (i+1, len(keys)):
                    if dict1[keys[i]] == dict1[keys[j]]:
                        temp.append(strs[keys[j]])
                        indexes.append(keys[j])
                    else:
                        pass

                result.append(temp)
        
        return result