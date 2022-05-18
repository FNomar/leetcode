class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j] + mat[i][j]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i-k), max(0, j-k), min(m, i+k+1), min(n, j+k+1)
                ans[i][j] = dp[r2][c2] - dp[r2][c1] - dp[r1][c2] + dp[r1][c1]
                
        return ans