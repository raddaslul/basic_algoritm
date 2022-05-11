from typing import List


class Solution:
    # 중첩함수를 이용하여 self 코드 생략 가능
    def numIslands(grid: List[List[str]]) -> int:
        def dfs(i, j):
            # 더 이상 땅이 아닌 경우(좌표를 벗어났거나 물이거나) 종료
            if i < 0 or i >= len(grid) or \
                    j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != "1":
                return
            grid[i][j] = "#"
            # 동서남북 탐색
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        count = 0
        # 주어진 grid 탐색
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1": # 해당 grid 좌표가 육지라면
                    dfs(i, j) # dfs 탐색
                    # 모든 육지 탐색 후 카운트 1 증가
                    count += 1
        return count

    result = numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
    print(result)
