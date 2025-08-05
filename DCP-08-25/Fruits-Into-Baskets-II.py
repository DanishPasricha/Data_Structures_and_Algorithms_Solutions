class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        c = 0
        flag = [False] * len(baskets)
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i] and flag[j] == False:
                    c+=1
                    flag[j] = True
                    break
        return len(baskets) - c