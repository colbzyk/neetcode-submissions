class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = None
        nums = sorted(nums)
        for n in nums:
            if prev == n:
                return prev
            prev = n
