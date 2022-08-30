"""
Time complexity: O(log(n)) insertion in ContinuousMedianHandler
Space complexity: O(n)

"""


def MAX_HEAP_FUNC(a, b):
    return a > b


def MIN_HEAP_FUNC(a, b):
    return a < b


class Heap:
    def __init__(self, comparison_func, array: 'list[int]') -> None:
        self.comparison_func = comparison_func
        self.heap = self.build_heap(array)
        self.length = len(self.heap)

    def build_heap(self, array: 'list[int]'):
        first_parent_idx = (len(array) - 2) // 2
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        return array
    
    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            # Define right child idx, if it exists.
            child_two_idx = current_idx * 2 + 2 if current_idx * 2 + 2 <= end_idx else -1
            # Child at idx 2 is smaller than child at idx 1. So, it should be swapped.
            if child_two_idx != -1:
                if self.comparison_func(heap[child_two_idx], heap[child_one_idx]):
                    idx_to_swap = child_two_idx
                else:
                    idx_to_swap = child_one_idx    
            else:
                idx_to_swap = child_one_idx
            
            # The child that have to be swapped is 
            # less than the current number that is checked, swap it.
            if self.comparison_func(heap[idx_to_swap], heap[current_idx]):
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return
    
    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0:
            if self.comparison_func(heap[current_idx], heap[parent_idx]):
                self.swap(current_idx, parent_idx, heap)
                current_idx = parent_idx
                parent_idx = (current_idx - 1) // 2
            else:
                return

    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.length -= 1
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        self.sift_up(len(self.heap) - 1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
   

class ContinuousMedianHandler:
    def __init__(self) -> None:
        self.median = None
        self.lowers = Heap(MAX_HEAP_FUNC, [])
        self.greaters = Heap(MIN_HEAP_FUNC, [])

    def insert(self, number: 'int'):
        if not self.lowers.length or number < self.lowers.peek():
            self.lowers.insert(number)
        else:
            self.greaters.insert(number)
        
        self.rebalance_heaps()
        self.update_median()
    
    def rebalance_heaps(self):
        if self.lowers.length - self.greaters.length == 2:
            self.greaters.insert(self.lowers.remove())
        elif self.greaters.length - self.lowers.length == 2:
            self.lowers.insert(self.greaters.remove())
        
    def update_median(self):
        if self.lowers.length == self.greaters.length:
            self.median = (self.lowers.peek() + self.greaters.peek()) / 2
        elif self.lowers.length > self.greaters.length:
            self.median = self.lowers.peek()
        else:
            self.median = self.greaters.peek()

    def get_median(self):
        return self.median


def main() -> None:
    MedianHandler = ContinuousMedianHandler()
    MedianHandler.insert(5)
    assert MedianHandler.get_median() == 5
    MedianHandler.insert(10)
    assert MedianHandler.get_median() == 7.5
    MedianHandler.insert(100)
    assert MedianHandler.get_median() == 10
    MedianHandler.insert(200)
    assert MedianHandler.get_median() == 55
    

if __name__ == '__main__':
    main()
