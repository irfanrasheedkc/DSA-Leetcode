class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        #Brute force
        result = []
        map = {}
        for i,n in enumerate(nums):
            if n==key:
                for j in range(i-k,i+k+1):
                    if j>=0 and j<len(nums):
                        if j not in map:
                            result.append(j)
                            map[j] = 1
        return result