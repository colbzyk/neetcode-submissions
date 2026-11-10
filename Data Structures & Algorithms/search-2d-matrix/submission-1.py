class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for curList in matrix:
            if target > curList[-1]:
                continue
            else:
                l, r = 0, len(curList)-1
                while l<=r:
                    m = (l+r)//2

                    if target > curList[m]:
                        l = m+1
                    elif target < curList[m]:
                        r = m-1
                    else:
                        return True
        return False