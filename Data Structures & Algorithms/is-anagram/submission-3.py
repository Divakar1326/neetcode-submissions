class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd=dict()
        td=dict()
        for ch in s:
            if ch in sd:
                sd[ch]+=1
            else:
                sd[ch]=1
        for cb in t:
            if cb in td:
                td[cb]+=1
            else:
                td[cb]=1
        res=True
        if len(sd)>=len(td):
            x=sd
        else:
            x=td
 #       print(sd, td)
        for k,v in x.items():
            if k in td and k in sd:
                if sd[k]!=td[k]:
                    res=False
                    break
            else:
                res=False
                break
        return res