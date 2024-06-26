class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals.sort(key=lambda i: i[0]) sorts the list of intervals 
        # lambda i: i[0] essentially tells the sort() method to use the first element of each interval as the criterion for sorting.
        
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]
        
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
                
        return output
            
            
        