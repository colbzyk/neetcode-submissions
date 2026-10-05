class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #[index, val]

        
        for i in range(len(heights)):
            ind = i
            while len(stack) != 0 and heights[i] <= stack[-1][1]:
                ind, val = stack.pop()
                area = val * (i - ind)
                if area > maxArea:
                    maxArea = area

            stack.append([ind, heights[i]])
        
        for i in range(len(stack)):
            area = stack[i][1] * (len(heights) - stack[i][0])
            if area > maxArea:
                maxArea = area

        return maxArea