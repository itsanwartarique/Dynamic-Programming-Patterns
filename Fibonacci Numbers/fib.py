class Solution:
    def fib(self, n: int) -> int:
        dp = [-1]*(n+1)
        def f(n):
            if dp[n] != -1:
                return dp[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            dp[n] = f(n-1) + f(n-2)
            return dp[n]
        result = f(n)
        return result