class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()

        def dfs(i):
            if i == n:
                return 

            visited.add(i)
            for j in range(n):
                if isConnected[i][j] and j not in visited:
                    dfs(j)

        count = 0
        for x in range(n):
            if x in visited:
                continue
            count += 1
            dfs(x)
        return count