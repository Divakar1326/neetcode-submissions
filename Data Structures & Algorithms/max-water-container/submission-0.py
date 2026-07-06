class Solution:
    def maxArea(self, heights: List[int]) -> int:
        current=0
        maxwater=-float("inf")
        i=0
        j=len(heights)-1
        while i<j:
            current=min(heights[i],heights[j])*(j-i)
            maxwater=max(maxwater,current)
            print(current,maxwater)
            if heights[i]>=heights[j]:
                j-=1
            else:
                i+=1
        return maxwater

        