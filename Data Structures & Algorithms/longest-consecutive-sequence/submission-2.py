class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashNums = set(nums)
        longest = 0
        for n in hashNums:
            if (n - 1) not in hashNums:
                length = 1
                while n + length in hashNums:
                    length += 1
                longest = max(length, longest)
        return longest
        