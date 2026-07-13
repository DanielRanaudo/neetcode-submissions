class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prevMap = {}
        for i in range(len(strs)):
            currWord = strs[i]
            #iterate through each char in currword
            count = [0]*26
            for char in currWord:
                count[ord(char) - ord('a')] += 1
            currFreq = tuple(count) #frequency of each char in currWord
            if currFreq in prevMap:
                prevMap[currFreq].append(currWord)
            #If it doesnt exist, create a new key
            else:
                prevMap[currFreq] = [currWord]
        #create a list of lists
        finList = []
        for l in prevMap:
            finList.append(prevMap[l])
        return finList

        