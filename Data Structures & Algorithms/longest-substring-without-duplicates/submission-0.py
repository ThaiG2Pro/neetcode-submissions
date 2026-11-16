class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=r = 0
        bucket = set()
        result = 0
        while  r < len(s):
            while s[r] in bucket :
                bucket.remove(s[l])
                l+=1
            
            bucket.add(s[r])
            r+=1
            result=max(result,r-l)
        return result