class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        q=deque()
        mx=[]
        l=0
        r=0
        while r <len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)
            while q and q[0]<l:
                q.popleft()
            if r-l+1==k:
                mx.append(nums[q[0]])
                l+=1
            r+=1
        return mx
            


