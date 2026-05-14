class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set1 = set()
        for num in nums:
            set1.add(num)
        return len(set1) != len(nums)