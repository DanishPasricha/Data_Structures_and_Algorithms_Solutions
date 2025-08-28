import heapq
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        d = {}

        for i in range(r):
            for j in range(c):
                key = i - j
                if key not in d: d[key] = []
                if key < 0: heapq.heappush(d[key], grid[i][j])
                else: heapq.heappush(d[key], -grid[i][j])

        for i in range(r):
            for j in range(c):
                key = i - j
                if key < 0: grid[i][j] = heapq.heappop(d[key])
                else: grid[i][j] = -heapq.heappop(d[key])
        return grid



# [
#     (0,0) , (0,1) , (0,2)
#     (1,0) , (1,1) , (1,2)
#     (2,0) , (2,1) , (2,2)

# ]