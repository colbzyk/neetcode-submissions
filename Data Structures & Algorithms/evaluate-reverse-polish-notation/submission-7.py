class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        set = ("+", "-", "/", "*")

        length = len(tokens)
        
        cache = []
        
        for t in range(len(tokens)):
            if tokens[t] in set:
                num2 = cache.pop()
                num1 = cache.pop()

                if tokens[t] == "*":
                    result = num1 * num2
                elif tokens[t] == "+":
                    result = num1 + num2
                elif tokens[t] == "-":
                    result = num1 - num2
                elif tokens[t] == "/":
                    result = int(num1 / num2)

                cache.append(result)

            else:
                cache.append(int(tokens[t]))

        return cache[-1]

                
                