class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap of frequencies
        freqHash = Counter(nums)
        freqList = sorted(freqHash.items(), key = lambda x :x[1])
        finList = []
        listLen = len(finList)
        for i in range(len(freqList) - k, len(freqList)):
            finList.append(freqList[i][0])

        return finList

        

        
        