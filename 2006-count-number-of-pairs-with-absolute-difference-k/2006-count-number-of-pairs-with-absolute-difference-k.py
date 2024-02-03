class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        prevMap = {}
        for i,n in enumerate(nums):
            if n+k in prevMap:
                count+=prevMap[n+k]
            if n-k in prevMap:
                count+=prevMap[n-k]
            
            if n in prevMap:
                prevMap[n]+=1
            else: 
                prevMap[n]=1
        return count