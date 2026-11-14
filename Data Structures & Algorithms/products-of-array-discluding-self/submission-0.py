class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        out1 = out2 = 1
        pre.append(out1)
        suf.append(out2)
        result = []
        n = len(nums)
        for i in range(n-1) :
            
            out1 = out1 * nums[i]
            pre.append(out1)

            out2 = out2 * nums[n-i-1]
            suf.append(out2)
        
        for i in range(n) :
            result.append ( pre[i]*suf[n-i-1] )

        return result

            