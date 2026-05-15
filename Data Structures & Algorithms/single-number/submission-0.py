class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) % 2 == 0:
            return 0
        nums.sort()
        i = 0
        while i < len(nums)-1: 
            if nums[i] != nums[i+1]:
                break
            i += 2
        return nums[i]