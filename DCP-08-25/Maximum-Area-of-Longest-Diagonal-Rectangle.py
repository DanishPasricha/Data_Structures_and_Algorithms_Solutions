class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d = {}
        ans_key = 0.0
        
        for l, b in dimensions:
            diagonal_length = math.sqrt((l*l) + (b*b))
            curr_area = l * b
            
            # Store max area for this diagonal
            if diagonal_length in d:
                d[diagonal_length] = max(d[diagonal_length], curr_area)
            else:
                d[diagonal_length] = curr_area
            
            ans_key = max(ans_key, diagonal_length)
        
        return d[ans_key]
