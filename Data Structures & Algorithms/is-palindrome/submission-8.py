class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = len(s) -1

        s = s.lower()

        for n in range(len(s)//2):
            if s[n].isalnum():
                while i >= 0 and not s[i].isalnum():
                    i-=1
                if s[n] != s[i]:
                    return False
                i-=1            
        return True



