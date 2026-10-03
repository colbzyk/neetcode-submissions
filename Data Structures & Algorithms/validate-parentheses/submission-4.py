class Solution:
    def isValid(self, s: str) -> bool:

        match = {"{":"}",
                "(":")",
                "[":"]"}
        
        stack = []

        for i in range(len(s)):
            if s[i] in match:
                stack.append(s[i])
            elif s[i] not in match and len(stack) != 0:
                if match[stack.pop()] == s[i]:
                    continue
                else:
                    return False
            else:
                return False
        return len(stack)==0

        
