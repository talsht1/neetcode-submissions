class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums: list[int] = sorted(nums)
        unique_counter_dict: dict[int, int] = {}
        unique_set_of_nums: set[int] = set()
        for num in sorted_nums:
            unique_set_of_nums.add(num)
        for num in unique_set_of_nums:
            unique_counter_dict[num] = nums.count(num)
        sorted_dict: dict[int, int] = dict(sorted(unique_counter_dict.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]