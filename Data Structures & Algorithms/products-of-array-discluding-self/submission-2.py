class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_prod = 1
        r_prod = 1
        res = [1] * len(nums)
        #Left to right
        for i in range(len(nums)):
            res[i] = l_prod
            l_prod *= nums[i]
        for j in range(len(nums) - 1, -1, - 1):
            res[j] *= r_prod
            r_prod *= nums[j]
        return res
       
       
       
        #Suboptimal Solution (Breaks division condition)
        output, prod, zero_count = [], 1, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                prod = prod * nums[i]

        
        for i in range(len(nums)):
            if zero_count > 1:
                output.append(0)
            elif zero_count == 1:
                if nums[i] != 0:
                    output.append(0)
                else:
                    output.append(prod)
            else:
                output.append(prod // nums[i])

        return output