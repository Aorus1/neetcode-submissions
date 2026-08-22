class MedianFinder:

    def __init__(self):
        self.left_max = []
        self.right_min = []
        self.left = 0
        self.right = 0

        

    def addNum(self, num: int) -> None:
        if (self.right) == 0: # if empty
            heapq.heappush(self.right_min, num)
            self.right += 1
        elif num > self.right_min[0]: # if should be on right
            heapq.heappush(self.right_min, num)
            self.right += 1
        else: # if should be on left
            heapq.heappush(self.left_max, -num)
            self.left += 1
        # balance
        if self.left > self.right + 1:
            heapq.heappush(self.right_min, -heapq.heappop(self.left_max))
            self.right += 1
            self.left -= 1
        elif self.right > self.left + 1:
            heapq.heappush(self.left_max, -heapq.heappop(self.right_min))
            self.left += 1
            self.right -= 1


        print([-x for x in self.left_max])
        print(self.left)
        print([x for x in self.right_min])
        print(self.right)
        print("\n")

        
            

                
                


        

    def findMedian(self) -> float:
        if (self.left + self.right == 1):
            return self.right_min[0]
        if (self.left + self.right) % 2 == 0: # if even
            return (-self.left_max[0] + self.right_min[0]) / 2
        else:
            if (self.left > self.right):
                return -self.left_max[0]
            else:
                return self.right_min[0]

        
        