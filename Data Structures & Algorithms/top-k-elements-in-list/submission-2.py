class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)

        result = []

        for _ in range(k):
            max_key = max(freq, key=freq.get)
            result.append(max_key)
            del freq[max_key]

        return result
