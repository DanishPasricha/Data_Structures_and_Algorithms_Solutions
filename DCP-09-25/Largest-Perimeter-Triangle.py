import math
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        k = sorted(nums)[::-1]
        for i in range(0,len(k)-2):
            x,y,z = k[i+1],k[i+2],k[i]
            if x+y>z:
                return x+y+z;   
        return 0