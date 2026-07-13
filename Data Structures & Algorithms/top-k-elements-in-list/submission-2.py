class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} 
        freq = [[] for i in range(len(nums) + 1)] #makes a list of lists of size len(nums)

        #counter function, then reverse it while simultaneously putting it
        #into list form
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        #result
        res = []
        for i in range(len(freq) - 1, 0, -1):
            #go one by one for i
            for n in freq[i]:
                res.append(n)
                if (len(res) == k): 
                    return res
                


            
        

        
        