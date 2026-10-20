class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        i = 0 
        while i < len(nums) - 1:
            max_jump = nums[i]

            best_index = 0
            max_range = 0
            if i + max_jump >= len(nums) - 1:
                return jumps + 1
            for j in range(min(i + 1, len(nums) - 1), min(i + max_jump + 1, len(nums))):
                ran = j + nums[j]
                if ran > max_range:
                    best_index = j
                    max_range = ran 
                
            i = best_index
            jumps += 1
        
        return jumps

        