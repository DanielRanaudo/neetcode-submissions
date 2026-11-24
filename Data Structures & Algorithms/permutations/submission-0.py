class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        def helper(currList):
            if len(currList) == len(nums):
                res.append(currList.copy())
                return

            for n in nums:
                if n in currList:
                    continue
                currList.append(n)
                helper(currList)
                currList.pop()

        helper([])
        return res

