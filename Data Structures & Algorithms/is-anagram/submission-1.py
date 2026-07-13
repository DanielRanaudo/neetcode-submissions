class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreq, tFreq = {}, {}
        for i in range(len(s)):
            sFreq[s[i]] = 1 + sFreq.get(s[i], 0)
            tFreq[t[i]] = 1 + tFreq.get(t[i], 0)
        
        for c in sFreq:
            if sFreq[c] != tFreq.get(c, 0):
                return False
        return True
# Everything Above is the final Soln
        sFreq = Counter(s)
        tFreq = Counter(t)
        return sFreq == tFreq
        