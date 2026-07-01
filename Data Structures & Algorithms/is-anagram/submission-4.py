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
        if sd==td:
            return True
        return False