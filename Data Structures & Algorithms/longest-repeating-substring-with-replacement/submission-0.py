class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l+r + hash (freq) + max
        # k vs  (r-l) - mostfreq

        l=0        
        bucket={}
        mostf=0
        result=0
        for r in range(len(s)):
            bucket[s[r]]=bucket.get(s[r],0)+1
            mostf=max(mostf,bucket[s[r]])

            if (r-l+1)-mostf > k :
                bucket[s[l]]-=1
                l+=1

            result = max(result,r-l+1)
        return result
