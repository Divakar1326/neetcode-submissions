class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        maxi=0
        l=0
        ans=0
        for r in range (len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxi=max(maxi,count[s[r]])
            winsize=r-l+1
            change=winsize-maxi
            while change>k:
                count[s[l]]-=1
                l+=1
                winsize=r-l+1
                change=winsize-maxi
            ans=max(ans,winsize)
        return ans

         
        