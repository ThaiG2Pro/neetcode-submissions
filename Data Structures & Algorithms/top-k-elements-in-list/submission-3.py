class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # hash : {num : freq} 
        # + sort by value -> get list of key, 
        bucket = {}
        for i in range(len(nums)):
            bucket[nums[i]] = bucket.get(nums[i], 0) + 1
        

        sorted_keys = sorted(bucket, key=bucket.get,reverse=True)        
        return      list(sorted_keys)[:k]


        