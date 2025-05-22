class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Approach:
        - Use dynamic programming to count unique paths from (0,0) to (m-1,n-1).
        - Create a 2D DP table where dp[i][j] represents the number of ways to reach cell (i,j).
        - Base Case:
            - The first row (dp[0][j]) and first column (dp[i][0]) must all be 1
              since there's only one way to reach those cells — by moving right or down.
        - For all other cells:
            - You can arrive at (i,j) from:
                - the cell above (i-1, j)
                - or the cell to the left (i, j-1)
            - So, dp[i][j] = dp[i-1][j] + dp[i][j-1]
        - The final result is stored in dp[m-1][n-1], the bottom-right cell.
        """

        # Create m x n grid filled with 1s (base case)
        dp = [[1] * n for _ in range(m)]

        # Fill the grid starting from cell (1,1)
        for i in range(1, m):
            for j in range(1, n):
                # Sum of paths from top and left
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]