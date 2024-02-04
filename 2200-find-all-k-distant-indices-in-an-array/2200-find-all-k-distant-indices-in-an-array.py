class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        map = {}
        for i,n in enumerate(nums):
            if n==key:
                for j in range(i-k,i+k+1):
                    if j>=0 and j<len(nums):
                        if j not in map:
                            map[j] = 1
        return map