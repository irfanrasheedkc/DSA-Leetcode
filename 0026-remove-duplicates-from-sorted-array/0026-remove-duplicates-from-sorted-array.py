class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newnums = {}
        for i,n in enumerate(nums):
            if n not in newnums:
                newnums[n]=1
        nums.clear()
        nums.extend(newnums)
        return len(nums)        