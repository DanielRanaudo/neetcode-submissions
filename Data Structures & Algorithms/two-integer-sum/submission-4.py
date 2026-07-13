class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #index, number at that index
        for i, n in enumerate(nums):
            if target - n in prevMap:
                return [prevMap[target - n], i]
            #if it doesnt exist we gotta add the value to map
            prevMap[n] = i
        return


        