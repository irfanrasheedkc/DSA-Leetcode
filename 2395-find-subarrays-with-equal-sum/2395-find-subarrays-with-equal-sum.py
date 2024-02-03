class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sumMap = {}
        for i in range(len(nums[:-1])):
            sum = nums[i]+nums[i+1]
            if sum in sumMap:
                return True
            sumMap[sum] = i
        return False