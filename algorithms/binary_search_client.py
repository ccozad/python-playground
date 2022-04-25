import math

class BinarySearchClient:
    # Items must be a sorted list of comparable items
    def __init__(self, items):
        if type(items) == list:
            self.items = items
        else:
            raise TypeError('items should be a list type')

    def find(self, target):
        start = 0
        end = len(self.items) - 1
        done = False
        result = None

        while not done:
            if start > end:
                done = True
            else:
                mid = math.floor((start + end)/2)

                if self.items[mid] < target:
                    start = mid + 1
                elif self.items[mid] > target:
                    end = mid - 1
                else:
                    done = True
                    result = mid
        
        return result

        