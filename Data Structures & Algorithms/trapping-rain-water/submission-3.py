class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        res = 0

        maxL, maxR = height[l], height[r]

        while l < r:
            if maxL <= maxR:
                res+= maxL - height[l]
                l+=1
                if height[l] > maxL:
                    maxL = height[l]
            else:
                res+= maxR - height[r]
                r-=1
                if height[r] > maxR:
                    maxR = height[r]    
        return res


            
            
            