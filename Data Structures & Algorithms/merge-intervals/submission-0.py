class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        for i in range(len(intervals) - 1):
            #take the start and finish times of interval[i]
            interval_at_i = intervals[i]
            i_start = interval_at_i[0]
            i_end = interval_at_i[1]

            #now, take the start and finish times of interval[i + 1]
            interval_at_j = intervals[i + 1]
            j_start = interval_at_j[0]
            j_end = interval_at_j[1]

            #check if they are overlapping, we know that i.s <= j.s, so we dont have to worry about that
            #merge if so
            if j_start <= i_end:
                new_interval = [i_start, max(j_end, i_end)]
                #now, we can remove interval_at_i, we can do this by making both vals neg
                intervals[i] = [-1, -1]
                intervals[i + 1] = new_interval
                #we change it in place, that way we dont have to worry about indexing issues

            #if they do not overlap, there is nothing to do 


        #now we have a list of intervals, but some may have negative vals (the ones we merged). We must remove them, we can do this instead by creating a new array
        res = []
        for i in range(len(intervals)):
            interval_at_i = intervals[i]
            #if start time is non-negative, add
            i_start = interval_at_i[0]
            if (i_start >= 0):
                res.append(interval_at_i)

        return res


        