class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #search the rows, then once we find the target row, binary search on that row

        #begin by binary searching on row, col = 0
        lo = 0
        hi = len(matrix) - 1
        def binarySearch(arr, target):
            low = 0
            high = len(arr) - 1
            mid = 0
            while low < high:
                mid = (high + low) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            
            return arr[low] == target


        while lo < hi:
            mid = (hi + lo) // 2

            val = matrix[mid][0]
            if mid + 1 >= len(matrix):
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] <= target < matrix[mid + 1][0]:
                return binarySearch(matrix[mid], target)
            elif matrix[mid][0] > target:
                hi = mid
            else:
                lo = mid + 1

        return binarySearch(matrix[lo], target)
        