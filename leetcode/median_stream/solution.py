import heapq

class MedianFinder(object):

    def __init__(self):
        # this is the "right" (bigger) number heap
        self._storage_min_heap = []

        # this is the "left" (smaller) number heap
        # to detect max will use negative number
        self._storage_max_heap = []

    def _push_left(self, num):
        heapq.heappush(self._storage_max_heap, -num)

    def _get_left(self):
        return -self._storage_max_heap[0]

    def _pop_left(self):
        return -heapq.heappop(self._storage_max_heap)

    def _push_right(self, num):
        heapq.heappush(self._storage_min_heap, num)

    def _pop_right(self):
        return heapq.heappop(self._storage_min_heap)
    
    def _get_right(self):
        return self._storage_min_heap[0]
    
    def _len_left(self):
        return len(self._storage_max_heap)

    def _len_right(self):
        return len(self._storage_min_heap)

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """

        if not self._storage_max_heap or self._get_left() > num:
            self._push_left(num)
        else:
            self._push_right(num)

        if self._len_left() > self._len_right() + 1:
            self._push_right(self._pop_left())
        elif self._len_right() > self._len_left() + 1:
            self._push_left(self._pop_right())


    def findMedian(self):
        """
        :rtype: float
        """
        if self._len_left() == self._len_right():
            return (self._get_left() + self._get_right()) / 2.    
        elif self._len_left() > self._len_right():
            return self._get_left()
        else:
            return self._get_right()
            

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()