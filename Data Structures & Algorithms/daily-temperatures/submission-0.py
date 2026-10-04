class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        

        for t in range(len(temperatures)):
            if  len(stack) == 0 or temperatures[t] < stack[-1][0]:
                stack.append([temperatures[t], t])
            else:
                while len(stack) != 0 and temperatures[t] > stack[-1][0]:
                    temp, index = stack.pop()
                    res[index] = t - index
                stack.append([temperatures[t], t])
                    
        return res

            