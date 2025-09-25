# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         dp = [math.inf for i in range(n)]
#         dp[0] = triangle[0][0]
#         for i in range(1,n):
#             dp[i] = dp[i-1] + min()
#         return sum
        

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for row in range(1, len(triangle)):
            for col in range(len(triangle[row])):
                triangle[row][col] = triangle[row][col] + min( triangle[row-1][col-1] 
                if col - 1 >= 0 else math.inf, triangle[row-1][col] 
                if col < len(triangle[row-1]) else math.inf)
	
        return min(triangle[-1])
        