class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        compHash = set(nums)
        return not len(compHash) == len(nums)

        