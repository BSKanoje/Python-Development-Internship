#Problem 973

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        distance = []
        for x, y in points:
            dist = x**2 + y**2
            distance.append((dist, (x, y))) 
        heapq.heapify(distance) 
        for i in range(k):
            ans.append(heappop(distance)[1]) 
        return ans