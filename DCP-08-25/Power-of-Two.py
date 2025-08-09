class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def is_integer_num(n):
            
            if isinstance(n, int):
                
                return True
            if isinstance(n, float):
                return n.is_integer()
            return False
        if n<=0:
            return False;
            

        if n==1:
            return True;
        if n%2==0 and (is_integer_num(log10(n)/log10(2))):
            return True;
        
        else:
            return False;