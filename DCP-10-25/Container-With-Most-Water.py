class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_area = 0
        while(i<=j):
            minimum = min(height[i],height[j])
            max_area = max(max_area,minimum*(j-i))
            if minimum == height[i]:
                i+=1
            if minimum == height[j]:
                j-=1
        return max_area

      