class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r - l
            height = min(heights[r], heights[l])
            if width * height > max_area:
                max_area = width * height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

        