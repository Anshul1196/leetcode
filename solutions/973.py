"""
Solution for Algorithms #973: K Closest Points to Origin

Runtime: 508 ms, faster than 14.68% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 18.1 MB, less than 9.90% of Python3 online submissions for K Closest Points to Origin.
"""
from heapq import heappush, heappushpop


class Point:
    def __init__(self, point):
        self.point = point
        self.neg_distance = -(point[0] ** 2 + point[1] ** 2)
    
    def __lt__(self, other):
        return self.neg_distance < other.neg_distance
    
    def __eq__(self, other):
        return self.neg_distance == other.neg_distance


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        closest_points = []
        for point in points:
            p = Point(point) # We use negative distance, so the head of min heap has the biggest distance

            # Fill the heap first
            if len(closest_points) < K:
                heappush(closest_points, p)
            else:
                # If closer point is found, pop biggest distance and add new point
                if p.neg_distance > closest_points[0].neg_distance:
                    heappushpop(closest_points, p)
        
        return [closest_point.point for closest_point in closest_points]
