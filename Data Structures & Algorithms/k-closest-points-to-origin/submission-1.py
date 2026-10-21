import random
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        #create an array computing the distances
        def distance(p):
            return math.sqrt(p[0]**2 + p[1]**2)

        #now we have an array of distances, we can do quickselect
        def quickselect(points, k):
            if len(points) <= k:
                return points

            pivot = random.choice(points)
            pivot_dist = distance(pivot)

            left = []
            right = []
            equal = []

            for p in points:
                if distance(p) < pivot_dist:
                    left.append(p)
                elif distance(p) == pivot_dist:
                    equal.append(p)
                else:
                    right.append(p)
            
            if len(left) >= k:
                return quickselect(left, k)
            if len(left) + len(equal) >= k:
                return left + equal[:k - len(left)]
            return left + equal + quickselect(right, k - (len(left) + len(equal)))
            
        return quickselect(points, k)