class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])

        #now, we can see if there are any overlapping intervals. Each time we see an overlap, we remove the larger one.
        res = 0
        end_time = 0
        for i in range(len(intervals) - 1):
            i_interval = intervals[i]
            i_start = i_interval[0]
            i_end = i_interval[1]

            j_interval = intervals[i + 1]
            j_start = j_interval[0]
            j_end = j_interval[1]

            #check for overlap
            if (j_start < i_end):
                #if there is overlap, remove the larger interval 
                if i_end <= j_end: #remove j
                    temp = intervals[i]
                    intervals[i] = [-1, -1]
                    intervals[i + 1] = temp
                    end_time = i_end
                else: 
                    end_time = j_end
                res += 1
        return res


