class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache: dict[tuple[int, int], int] = {}

        def move(row: int, col: int) -> int:
            if (row, col) in cache:
                return cache[(row, col)]
            if row == m - 1 and col == n - 1:
                return 1
            if row >= m or col >= n:
                return 0
            cache[(row, col)] = move(row + 1, col) + move(row, col + 1)
            return cache[(row, col)]

        return move(0, 0)