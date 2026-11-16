class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        result = 0
        while l<r:
            cal = (r-l)*min(heights[r],heights[l])
            result = max (result,cal)

            if heights[l] > heights[r] :
                r-=1
            else : l+=1

        return result


# r-l * min(l,r)
# max(l+1,r-1) 
# r-l-1 * h = r-l*h - h