#RAT IN A MAZE   
class Solution:
    def ratInMaze(self, maze: list[list[int]]) -> list[str]:
        n = len(maze)
        result = []

        if maze[0][0] == 0:
            return result

        visited = [[False] * n for _ in range(n)]

        def solve(row, col, path):
            if row == n - 1 and col == n - 1:
                result.append(path)
                return

            visited[row][col] = True

            # Down
            if row + 1 < n and maze[row + 1][col] == 1 and not visited[row + 1][col]:
                solve(row + 1, col, path + "D")

            # Left
            if col - 1 >= 0 and maze[row][col - 1] == 1 and not visited[row][col - 1]:
                solve(row, col - 1, path + "L")

            # Right
            if col + 1 < n and maze[row][col + 1] == 1 and not visited[row][col + 1]:
                solve(row, col + 1, path + "R")

            # Up
            if row - 1 >= 0 and maze[row - 1][col] == 1 and not visited[row - 1][col]:
                solve(row - 1, col, path + "U")

            visited[row][col] = False

        solve(0, 0, "")
        return sorted(result)