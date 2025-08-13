class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False;
        if n==1:
            return True;
        if ((log10(n)/log10(3)).is_integer()):
            return True; 
        else:
            return False;
        