class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        lowest = r

        while l<=r:
            m = (l+r) // 2
            time = 0

            for p in piles:
                time+= math.ceil(p/m)
                if h-time == h:
                    h-=1
            
            if h-time >= 0:
                if m<lowest:
                    lowest = m
                r = m-1
            elif h-time < 0:
                l = m+1  

        return lowest
            
            

            

            
                
            
            

        

        