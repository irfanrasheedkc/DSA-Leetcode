class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newnums = []
        for i in range(len(nums)):
            if nums[i] not in newnums:
                newnums.append(nums[i])
        nums.clear()
        nums.extend(newnums)
        return len(nums)        