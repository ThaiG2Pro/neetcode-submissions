class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        new_n = sorted(nums)
        n = len(new_n)
        for i in range(n-2):
            # if nums[i] == nums[i-1] : continue
            l,r = i+1, n-1
            while l<r:
                # if num[l] == num[+1]
                sum3 = new_n[i] + new_n[l] + new_n[r]
                if sum3 == 0 : 
                    result.add(tuple([new_n[i],new_n[l],new_n[r]]))
                    l+=1
                elif sum3 < 0:
                    l+=1
                    # while new_n[l] == new_n[l-1] :
                    #     l+=1
                elif sum3 > 0:
                    r-=1
                    # while new_n[r] == new_n[r+1] :
                    #     r-=1                 

        return list(result)


# -4 -1 -1 0 1 2
#  0  1  2 3 4 5
#  n = 6
#  1,3,4