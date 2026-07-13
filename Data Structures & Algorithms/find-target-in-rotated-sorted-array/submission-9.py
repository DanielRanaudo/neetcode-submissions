class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        return self.searchHelper(nums, target, 0, len(nums) - 1)
    
    def searchHelper(self, nums: List[int], target: int, left: int, right: int) -> int:
        if abs(left - right) <= 1: 
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            else: 
                return -1
        

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[right] == target:
            return right
        elif nums[left] == target:
            return left

        #left half is sorted
        if nums[left] < nums[mid]:
            if nums[left] <= target < nums[mid]:
                return self.searchHelper(nums, target, left, mid)
            else: 
                return self.searchHelper(nums, target, mid, right)
        else: #right half is sorted
            if nums[mid] <= target and nums[right] >= target:
                return self.searchHelper(nums, target, mid, right)
            else: 
                return self.searchHelper(nums, target, left, mid)
            