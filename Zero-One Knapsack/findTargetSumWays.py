class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        curr_sum = 0
        cache = {}
        def dp(nums,target,index,curr_sum):
            if (index,curr_sum) in cache:
                return cache[(index,curr_sum)]
            #base case
            if index<0 and curr_sum == target:
                return 1
            if index< 0:
                return 0
            #decisions 
            positive = dp(nums,target,index-1,curr_sum + nums[index])
            negative = dp(nums,target,index-1,curr_sum - nums[index])
            
            #Calculations
            cache[(index,curr_sum)] = positive + negative
            return cache[index,curr_sum]
        return dp(nums,target,len(nums)-1,curr_sum)