class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2

        l, r = 0, len(nums1)-1

        while True:
            m = (l+r) // 2
            
            j = half - (m+1) - 1

            Oneleft = nums1[m] if m >= 0 else float("-infinity")
            Oneright = nums1[m+1] if (m+1) < len(nums1) else float("infinity")
            Twoleft = nums2[j] if j >= 0 else float("-infinity")
            Tworight = nums2[j+1] if (j+1) < len(nums2) else float("infinity")

            if Oneleft <= Tworight and Twoleft <= Oneright:
                if total % 2:
                    return min(Oneright, Tworight)
                else:
                    return (max(Oneleft, Twoleft) + min(Oneright, Tworight)) / 2
            elif Oneleft > Tworight:
                r = m - 1
            elif Twoleft > Oneright:
                l = m + 1


            
