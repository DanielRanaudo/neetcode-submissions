class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) == 0:
            return False
        comp = nums[0]
        for x in nums [1:]:
            if x == comp:
                return True
            else:
                comp = x
        return False

        