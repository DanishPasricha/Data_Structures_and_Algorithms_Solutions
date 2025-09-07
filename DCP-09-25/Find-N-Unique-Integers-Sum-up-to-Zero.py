class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []

        pairs = n // 2
        for i in range(1, pairs + 1):
            ans.append(i)
            ans.append(-i)

        if n % 2 == 1: ans.append(0)
            
        return ans