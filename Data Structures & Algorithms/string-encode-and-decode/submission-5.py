class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in range(len(strs)):
            s+=strs[i]
            s+="."
        return s


    def decode(self, s: str) -> List[str]:
        res=[]
        word=""
        for ch in s:
            if ch ==".":
                res.append(word)
                word=""
            else:
                word+=ch
        s=""
        return res