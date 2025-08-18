from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        TARGET = 24.0

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPS

            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):   # ✅ only pick i < j to avoid duplicate pairs
                    next_nums = []
                    for k in range(n):
                        if k != i and k != j:
                            next_nums.append(nums[k])

                    a, b = nums[i], nums[j]

                    # collect all possible candidate results
                    candidates = []
                    candidates.append(a + b)
                    candidates.append(a - b)
                    candidates.append(b - a)
                    candidates.append(a * b)

                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        # convert to float up front
        new_list = []
        for x in cards:
            new_list.append(float(x))

        return dfs(new_list)
