class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            for sub in res[:]:
                res.append(sub + [n]) 
        
        return res
