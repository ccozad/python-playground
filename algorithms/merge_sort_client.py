import math

class MergeSortClient:
    def __init__(self, items):
        self.items = items.copy()
    
    def sort(self):
        return self._mergesort(self.items)
    
    def _mergesort(self, list):
        if len(list) <= 1:
            return list
        else:
            middle = math.floor(len(list) / 2)
            left = list[0:middle]
            right = list[middle:]
            left = self._mergesort(left)
            right = self._mergesort(right)
            if left[-1] <= right[0]:
                left = left + right
                return left
            
            result = self._merge(left, right)
            return result

    def _merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        if len(left) > 0:
            result = result + left
        
        if len(right) > 0:
            result = result + right
        
        return result