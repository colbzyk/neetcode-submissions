class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        res = 0

        while l < r:
            if (min(heights[l], heights[r]) * (r-l)) > res:
                res = min(heights[l], heights[r]) * (r-l)

            if heights[l] > heights[r]:
                r-=1
            elif heights[r] > heights[l]:
                l+=1
            else:
                l+=1
                r-=1            
        return res
        


