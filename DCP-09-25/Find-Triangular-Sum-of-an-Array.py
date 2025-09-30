class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        dp=[]
        n=len(nums)
        
        while(n!=0):
            s_dp=[0]*n
            dp.append(s_dp)
            n-=1

        dp[0]=nums
        for i in range(1,len(dp)):
            for j in range(len(nums)-i):
                dp[i][j]= (dp[i-1][j] + dp[i-1][j+1]) % 10
        
        return dp[-1][0]