class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        #Brute force
        map = {}
        for i,n in enumerate(nums):
            if n==key:
                for j in range(i,i-k-1,-1):
                    if j>=0:
                        if j not in map:
                            map[j] = 1
                        else:
                            break
                for j in range(i+1,i+k+1):
                    if j<len(nums):
                        if j not in map:
                            map[j] = 1

        return sorted(map)