import math
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        def binary_search(min_req,potions):
            start = 0
            end = len(potions) 
       
            while (start < end):
                mid = (start + end)//2
                if potions[mid]>=min_req:
                    end = mid

                else:
                    start = mid+1
                   

            return start

        pairs = []
        potions = sorted(potions) 
        m = len(potions)
        for i in range(len(spells)):
            min_req = ((success + spells[i] - 1)//spells[i]) 
            index = binary_search(min_req,potions)
            if potions[-1] < min_req:
                pairs.append(0)
            else: 
                pairs.append(m - index)
        return pairs





