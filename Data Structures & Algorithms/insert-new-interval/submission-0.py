class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart = newInterval[0]
        newEnd = newInterval[1]
        res = []
        res.insert(0, newInterval)
        j = 0

        for i in range(len(intervals)):
            intvl = intervals[i]
            s = intvl[0] #start
            e = intvl[1] #end 

            #cases
            if e < newStart:
                res.insert(j, intvl)
                j += 1
            elif s > newEnd:
                res.append(intvl)
            
            else:
                newStart = min(s, newStart)
                newEnd = max(e, newEnd)
                res[j] = [newStart, newEnd]

        return res




                    
 