class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        d2 = {}
        for k,v in d.items():
            if v not in d2:
                d2[v] = [k]
            else:
                d2[v].append(k)

        d2_reverse = sorted(d2.keys(), reverse=True)
        sorted_dict_reverse = {key: d2[key] for key in d2_reverse}        
        
        first_key = next(iter(sorted_dict_reverse))
        first_value = sorted_dict_reverse[first_key]
        
        return first_key * len(first_value)