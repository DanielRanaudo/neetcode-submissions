class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Get all the starting blocks, put them on the dict
        finSet, longest = set(nums), 0
        for n in finSet:
            if n - 1 not in finSet: #start of new block
                length = 0
                while n + length in finSet:
                    length += 1
                if length > longest:
                    longest = length
        
        return longest

            
















        finSet = set(nums)
        longestSeq = 0
        startInt = 0
        for n in finSet:
            if n - 1 not in finSet:
                startInt = n
            elif n - 1 == startInt:
                longestSeq += 1
                startInt = n
                


        for n in nums:
            if n - 1 in finSet or n + 1 in finSet:
                finSet.add(n)
        for n in reverse(nums):
            if n - 1 in finSet or n + 1 in finSet:
                finSet.add(n)

