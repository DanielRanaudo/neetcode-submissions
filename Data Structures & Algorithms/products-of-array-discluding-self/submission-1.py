class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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