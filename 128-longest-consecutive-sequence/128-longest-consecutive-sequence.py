class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        
        max_len = 0
        
        for n in nums:
            if n-1 in nums:
                continue
                
            curr_len = 1
                
            while n+curr_len in nums:
                curr_len += 1
                
            max_len = max(max_len, curr_len)
            
        return max_len
    