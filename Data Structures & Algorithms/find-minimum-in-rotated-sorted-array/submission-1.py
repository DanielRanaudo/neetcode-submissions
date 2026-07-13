class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        mid = len(nums) // 2
        if len(nums) == 1:
            return nums[0]

        #base case
        if len(nums) <= 2:
            return min(nums[0], nums[1])

        #otherwise, recursively call
        if nums[mid] > nums[r]:
            return self.findMin(nums[mid:])
        else: 
            return self.findMin(nums[:mid + 1])




        