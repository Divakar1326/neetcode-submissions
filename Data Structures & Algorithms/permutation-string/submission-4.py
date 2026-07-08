class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1=dict()
        ds2=dict()
        if len(s1) > len(s2):
            return False
        for ch in s1:
            ds1[ch]=ds1.get(ch,0)+1
        for i in range (len(s1)):
            ds2[s2[i]]=ds2.get(s2[i],0)+1
        l=0
        r=len(s1)-1
        while r<len(s2)-1:
            print(ds1,ds2)
            if ds1==ds2:
                return True
            else:
                ds2[s2[l]] -= 1
                if ds2[s2[l]] == 0:
                    del ds2[s2[l]]
                l+=1
                r+=1
                ds2[s2[r]]=ds2.get(s2[r],0)+1
        return ds1==ds2

