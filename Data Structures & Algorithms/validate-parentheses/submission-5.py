class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        if len(s)<=1:
            return False
        for ch in s :
            if not ans and ch in ")}]":
                return False
            if ch in "({[":
                ans.append(ch)
            else:
                if ans and ch ==")" and ans[-1]=="(":
                    ans.pop()
                elif ans and ch =="}" and ans[-1]=="{":
                    ans.pop()
                elif ans and ch =="]" and ans[-1]=="[":
                    ans.pop()
                else:
                    return False
        print(ans)
        return not bool(ans)




        