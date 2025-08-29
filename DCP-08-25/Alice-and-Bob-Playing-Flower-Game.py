class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return n * m // 2


# Intuition
# The outcome depends only on whether the numbers of flowers are odd or even. 
# Alice wins if one lane has an odd number of flowers and the other lane has an even number.


# Approach
# There are n * m total possible pairs. 
# Exactly half of them will have different parity (one odd, one even). 
# Therefore the answer is n * m / 2.


# Complexity
# Time complexity:O (1)
# Space complexity: O (1)


