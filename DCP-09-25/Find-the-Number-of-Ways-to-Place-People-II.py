class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))  # sort by x asc, y desc
        n = len(points)
        result = 0

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if y2 <= y1:  # must be valid direction
                    valid = True
                    # check only points between i and j
                    for k in range(i+1, j):
                        xk, yk = points[k]
                        if x1 <= xk <= x2 and y2 <= yk <= y1:
                            valid = False
                            break
                    if valid:
                        result += 1

        return result
