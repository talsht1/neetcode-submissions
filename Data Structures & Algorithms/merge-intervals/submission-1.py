class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_array: list[list[int]] = []
        if len(intervals) == 1:
            return intervals
        sorted_intervals_array = sorted(intervals, key=lambda interval: interval[0])
        for interval in sorted_intervals_array:
            if len(new_array) == 0:
                new_array.append(interval)
            elif interval[0] <= new_array[-1][1]:
                new_array[-1][1] = max(new_array[-1][1], interval[1])
            else:
                new_array.append(interval)
        return new_array