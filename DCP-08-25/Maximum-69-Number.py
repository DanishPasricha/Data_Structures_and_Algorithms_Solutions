class Solution:
    def maximum69Number(self, num: int) -> int:
        temp = num
        index = -1
        pos = 0

        while temp > 0:
            if temp % 10 == 6:
                index = pos
            temp //= 10
            pos += 1

        return num if index == -1 else num + 3 * (10 ** index)