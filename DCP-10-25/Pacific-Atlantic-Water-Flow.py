class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        
        p_visited=set();
        a_visited=set();
        
        def dfs(row,col,visited,curr):
            if row<0 or row>=m or col<0 or col>=n or (row,col) in visited or grid[row][col]<curr: return
            
            visited.add((row,col))
            
            
            dfs(row+1,col,visited,grid[row][col]);
            dfs(row-1,col,visited,grid[row][col]);
            dfs(row,col-1,visited,grid[row][col]);
            dfs(row,col+1,visited,grid[row][col]);
            
        for col in range(n):
            dfs(0,col,p_visited,grid[0][col])
            dfs(m-1,col,a_visited,grid[m-1][col])
            
        for row in range(m):
            dfs(row,0,p_visited,grid[row][0])
            dfs(row,n-1,a_visited,grid[row][n-1])
            
            
        ans=[];
        for i in range(m):
            for j in range(n):
                if (i,j) in p_visited and (i,j) in a_visited:
                    ans.append([i,j])
        return ans