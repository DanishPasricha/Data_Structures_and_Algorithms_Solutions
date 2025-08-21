from collections import deque

class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        
        # heights[j] = number of consecutive 1s ending at current row in column j
        heights = [0] * n  
        ans = 0
        
        for i in range(m):  
            for j in range(n):
                if mat[i][j] == 0:
                    heights[j] = 0   # reset if zero
                else:
                    heights[j] += 1  # stack the height of consecutive 1s

            # Now count rectangles with histogram (like largest rectangle in histogram problem)
            ans += self.countRectangles(heights)
        
        return ans
    
    def countRectangles(self, heights):
        """
        Count rectangles using monotonic stack:
        For each column, count how many rectangles end at this column.
        """
        stack = deque()   # store indices
        dp = [0] * len(heights)  # dp[j] = rectangles ending at column j
        total = 0

        for j, h in enumerate(heights):
            # maintain increasing stack
            while stack and heights[stack[-1]] >= h:
                stack.pop()
            
            if stack:
                prev = stack[-1]
                dp[j] = dp[prev] + h * (j - prev)
            else:
                dp[j] = h * (j + 1)
            
            stack.append(j)
            total += dp[j]
        
        return total
