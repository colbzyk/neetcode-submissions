class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counterS = {}
        counterT = {}

        for n in range(len(s)):
            counterS[s[n]] = 1 + counterS.get(s[n], 0)
            counterT[t[n]] = 1 + counterT.get(t[n], 0)
        for j in counterS:
            if counterS[j] != counterT.get(j, 0):
                return False
        return True
