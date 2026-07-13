class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        currLen = 0
        longest = 0
        substr = set()
        for right in range(len(s)): 
            while s[right] in substr:
                substr.remove(s[left])
                left += 1
            # Now that its removed, add the next
            substr.add(s[right])
            longest = max(longest, right - left + 1)

            if currLen > longest:
                longest = currLen
            
        return longest