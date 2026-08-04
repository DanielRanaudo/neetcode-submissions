class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        curr = []
        def dfs(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            if currSum > target or i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i, currSum + nums[i])
            curr.pop()

            dfs(i + 1, currSum)
                

        dfs(0, 0)
        return res