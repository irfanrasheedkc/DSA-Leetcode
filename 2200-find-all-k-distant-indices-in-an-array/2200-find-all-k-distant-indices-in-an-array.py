class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        #Brute force
        result = set()
        for i,n in enumerate(nums):
            if n==key:
                for j in range(i-k,i+k+1):
                    if j>=0 and j<len(nums):
                        result.add(j)
        return result