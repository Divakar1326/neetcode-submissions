class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxlen=0
        currentlen=0
        store=set()
        while r<len(s):
            if s[r]not in store:
                store.add(s[r])
                r+=1
            else:
                store.remove(s[l])
                l+=1


            currentlen=max(currentlen,r-l)
            maxlen=max(maxlen,currentlen)
        return maxlen
            

        