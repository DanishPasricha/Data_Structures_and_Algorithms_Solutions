from functools import lru_cache
from typing import List, Tuple

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        # Diagonal directions in clockwise order:
        #  ↘ (down-right), ↙ (down-left), ↖ (up-left), ↗ (up-right)
        directions: List[Tuple[int, int]] = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

        # Next required value along a valid segment: 1 → 2 → 0 → 2 → 0 → ...
        next_value = {1: 2, 2: 0, 0: 2}

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < rows and 0 <= j < cols

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, d_index: int, turned: bool) -> int:
            """
            Longest segment length starting at (i, j), initially moving in
            direction `d_index`, having used the single clockwise turn iff `turned`.
            Counts the current cell as length 1.
            """
            if not in_bounds(i, j):
                return 0

            best = 1  # include current cell

            # Continue straight
            di, dj = directions[d_index]
            ni, nj = i + di, j + dj
            required = next_value[grid[i][j]]
            if in_bounds(ni, nj) and grid[ni][nj] == required:
                best = max(best, 1 + dfs(ni, nj, d_index, turned))

            # Use the single clockwise turn (if available)
            if not turned:
                nd_index = (d_index + 1) % 4  # clockwise 90° turn
                ndi, ndj = directions[nd_index]
                ti, tj = i + ndi, j + ndj
                if in_bounds(ti, tj) and grid[ti][tj] == required:
                    best = max(best, 1 + dfs(ti, tj, nd_index, True))

            return best

        answer = 0
        # Start only from cells with value 1 (per problem)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1:
                    continue
                for d in range(4):
                    answer = max(answer, dfs(i, j, d, False))
        return answer
