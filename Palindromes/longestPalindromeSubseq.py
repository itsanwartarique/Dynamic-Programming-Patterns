class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        a = s
        b = s[::-1]
        m = len(a)
        n = len(b)
        res =''
        memo = [[-1]*(m+1) for i in range(n+1)]
        def lcs(a,b,m,n):
            if memo[m][n] != -1:
                return memo[m][n]
            # Base case
            if m == 0 or n == 0:
                return 0
            if a[m-1] == b[n-1]:
                memo[m][n] = 1 + lcs(a[:m-1],b[:n-1],m-1,n-1)
            else:
                memo[m][n] = max(lcs(a[:m-1], b, m-1, n),lcs(a,b[:n-1], m, n-1))
            return memo[m][n]
        result = lcs(a,b,m,n)
        return result


                
            