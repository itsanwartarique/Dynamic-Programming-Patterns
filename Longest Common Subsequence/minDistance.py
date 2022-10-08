class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def helper(word1,word2,m,n):
            # Base Case
            if m == 0:
                return n
            if n == 0:
                return m
            #look up
            if (m-1,n-1) in cache:
                return cache[(m-1,n-1)]
            #Decisions
            if word1[m-1] == word2[n-1]:
                return helper(word1,word2,m-1,n-1)
            
            insert = helper(word1,word2,m,n-1)
            delete = helper(word1,word2,m-1,n)
            replace = helper(word1,word2,m-1,n-1)

            #Calcultaions
            cache[(m-1,n-1)] = 1 + min(insert,delete,replace)
            return cache[(m-1,n-1)]
        return helper(word1,word2,len(word1),len(word2))