class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for _ in range (len(nums)+1)]
        count={}
        for num in nums:
           count[num]=count.get(num,0)+1
        for key,v in count.items():
            bucket[v].append(key)
        result=[]
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)

                if len(result) == k:
                    return result
        