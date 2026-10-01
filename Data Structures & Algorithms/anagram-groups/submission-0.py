class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26 #26 letters of the alphabet

            for i in s:
                count[ord(i) - ord("a")] += 1

            groups[tuple(count)].append(s)
        
        return list(groups.values())

        