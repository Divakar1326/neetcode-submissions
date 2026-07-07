class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax=[0]*len(height)
        rightmax=[0]*len(height)
        maxi=0
        for i in range (0,len(height)):
            leftmax[i]=max(leftmax[i-1],height[i])
        print(leftmax)
        rightmax[len(height)-1]=height[-1]
        for j in range(len(height)-2,-1,-1):
            rightmax[j]=max(rightmax[j+1],height[j])
        print(rightmax)
        water=0
        for k in range (len(height)):
            water+=min(leftmax[k],rightmax[k])-height[k]
        return water

            
        