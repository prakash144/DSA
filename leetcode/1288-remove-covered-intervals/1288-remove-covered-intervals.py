class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))  # Sort intervals by start time in ascending order and end time in descending order
        count = 0
        end = float('-inf')
        

        for start, curr_end in intervals:
            if curr_end > end: 
                end = curr_end  
                count += 1 

        return count