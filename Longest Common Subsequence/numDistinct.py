class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #brute force 
        # count = [0]
        # def helper(ip,op,t):
        #     #base case
        #     if len(ip) == 0:
        #         if op == t:
        #             count[0] +=1
        #         return
        #     op1 = op
        #     op2 = op
        #     op2 += ip[0]
        #     helper(ip[1:], op1,t)
        #     helper(ip[1:], op2,t)
        # helper(s,'',t)
        # return count[0]
        
        #recursion
        # def helper(s,t,m,n):
        #     if n == 0:
        #         return 1
        #     if m == 0:
        #         return 0
        #     temp1 = 0
        #     if s[m-1] == t[n-1]:
        #         temp1 = helper(s,t,m-1,n-1)
        #     temp2 = helper(s,t,m-1,n)
        #     return temp1 + temp2
        # return helper(s,t,len(s),len(t))
        
        #recursion + memoization
        cache = {}
        def helper(s,t,m,n):
            if n == 0:
                return 1
            if m == 0:
                return 0
            if (m-1,n-1) in cache:
                return cache[(m-1,n-1)]
            temp1 = 0
            if s[m-1] == t[n-1]:
                temp1 = helper(s,t,m-1,n-1)
            temp2 = helper(s,t,m-1,n)
            cache[(m-1,n-1)] = temp1 + temp2
            return cache[(m-1,n-1)]
        return helper(s,t,len(s),len(t))
        
    