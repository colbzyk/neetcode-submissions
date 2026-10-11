class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1

        max = 0

        mult = len(heights)-1

        while l < r:
            if (min(heights[l], heights[r]) * mult) > max:
                max = min(heights[l], heights[r]) * mult


            if heights[l] > heights[r]:
                r-=1
                mult-=1
            elif heights[r] > heights[l]:
                l+=1
                mult-=1
            else:
                l+=1
                r-=1
                mult-=2
            

        return max
        


