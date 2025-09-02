class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        n = len(points)
        result = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                x1, y1 = points[i]
                x2, y2 = points[j]

                # i must not be to the right of j
                if (x1 < x2 or x1 == x2) and y2 <= y1:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break

                    if valid:
                        result += 1

        return result
