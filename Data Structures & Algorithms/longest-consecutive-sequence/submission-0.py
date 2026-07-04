class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        maxc=0
        for num in nums:
            count=1
            if num-1 not in nums:
                s=num+1
                while s in nums:
                    count+=1
                    s+=1
                maxc=max(maxc,count)
        return maxc

        