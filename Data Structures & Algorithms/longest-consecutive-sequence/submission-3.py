class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0 : return 0
        bucket = set(nums)
        
        count = 1
        for i in range(len(nums)):                
            if (nums[i]-1) not in bucket :
                j = 1
                while (nums[i]+j) in bucket :
                   j+=1
                count = max(count,j)

        return count