import heapq
from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #begin by sorting by start time
        intervals.sort(key=lambda x: x.start)

        earliest_finish = []
        earliest_finish.append(float('inf'))

        #maintain a counter for how many rooms we need
        count = 0

        #iterate throguh all, keeping count of how many times we need to create a new room
        #new rooms are created when earliest finish is greater than next start
        for i in range(len(intervals)):
            #place the earliest start time in its own, then take its finish time, record it as a variable
            curr_interval = intervals[i]
            curr_start = curr_interval.start
            curr_fin = curr_interval.end

            #if we force a collision, we create a new room
            if (curr_start < earliest_finish[0]):
                count += 1
                heapq.heappush(earliest_finish, curr_fin)
            #otherwise, we extned the earliest room
            else:
                heapq.heappop(earliest_finish)
                heapq.heappush(earliest_finish, curr_fin)

        return count