class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def largestRectangleArea(self, height):
        stack=[]; i=0; area=0
        while i<len(height):
            if stack==[] or height[i]>height[stack[len(stack)-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                width=i if stack==[] else i-stack[len(stack)-1]-1
                area=max(area,width*height[curr])
                i-=1
            i+=1
        while stack!=[]:
            curr=stack.pop()
            width=i if stack==[] else len(height)-stack[len(stack)-1]-1
            area=max(area,width*height[curr])
        return area
        
    def maximalRectangle(self, matrix):
        if matrix==[]: return 0
        a=[0 for i in range(len(matrix[0]))]; maxArea=0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                a[j]=a[j]+1 if matrix[i][j]=='1' else 0
            
            maxArea=max(maxArea, self.largestRectangleArea(a))
        
        return maxArea