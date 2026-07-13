class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        longest = 0
        for n in hashNums:
            currNum = n
            currLength = 1
            while currNum + 1 in hashNums:
                currLength += 1
                currNum += 1
            if currLength > longest:
                longest = currLength
        return longest
        