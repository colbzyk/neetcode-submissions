class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        hours = h
        lowest = None

        while l<=r:
            m = (l+r) // 2
            h = hours
            for p in piles:
                h-= math.ceil(p/m)
                if h == hours:
                    h-=1

            if h >= 0:
                if lowest == None or m<lowest:
                    lowest = m
                r = m-1
            elif h < 0:
                l = m+1  

        return lowest
            
            

            

            
                
            
            

        

        