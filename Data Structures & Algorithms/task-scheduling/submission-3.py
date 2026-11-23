class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freq = {}
        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
        
        #sort, takes O(1) time since there are only 23 letts in alphabet
        sortedFreq = sorted(freq.items(), key=lambda x: x[1], reverse = True)
        maxTime = 0

        for i in range(len(sortedFreq)):
            char, appears = sortedFreq[i]
            
            maxTime = max(maxTime, i + 1 + (1 + n) * (appears - 1))

        return max(maxTime, len(tasks))