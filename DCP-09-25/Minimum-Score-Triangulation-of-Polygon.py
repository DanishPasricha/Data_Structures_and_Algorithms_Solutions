class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        def dfs(i, j):
            # base; same index
            if i == j - 1:
                return 0
            # seen before
            if (i, j) in memo:
                return memo[(i, j)]
            # otherwise, compute memo[(i, j)]
            res = float('inf')
            # split values[i: j] into values[i: k] and values[k : j] 
            for k in range(i + 1, j):
                temp = values[i] * (values[j] * values[k]) + dfs(i, k) + dfs(k, j)
                # update res 
                res = min(res, temp)
            # update
            memo[(i, j)] = res
            return memo[(i, j)]
        
        n = len(values)
        # memo[(i, j)] := minimum possible score that you can achieve with some triangulation of the polygon in values[i: j]
        memo = dict()
        return dfs(0, n - 1) 