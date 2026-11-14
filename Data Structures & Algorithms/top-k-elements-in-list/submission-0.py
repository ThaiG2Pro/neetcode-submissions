class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        for i in range(len(nums)) :
            if nums[i] in bucket: 
                bucket[nums[i]] = bucket.get(nums[i],0)+1
            else : bucket[nums[i]] = 1
        

        sorted_keys = sorted(bucket, key=bucket.get,reverse=True)        
        return      list(sorted_keys)[:k]


        