class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic=dict()
        for el in nums:
            if el in dic:
                return True
            else:
                 dic[el] = 1
        return False
        