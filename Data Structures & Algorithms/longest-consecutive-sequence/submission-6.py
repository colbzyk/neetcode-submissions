class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        seen = set()
        seqs = Counter()

        for n in nums:
            seen.add(n)
        
        n = 0
        for n in seen:
            current = n

            if n-1 not in seen:
                seqs[n] += (1)
                while current+1 in seen:
                    seqs[n] += (1)
                    current+=1
            n+=1
            
        
        pair = seqs.most_common(1)
        key, val = pair[0]

        return val
