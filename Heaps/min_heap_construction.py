"""
Time complexity: O(n)
Space complexity: O(1)

Heap:
    parent_idx = (len(array) - 2) // 2
    
    left_idx = idx * 2 + 1
    right_idx = idx * 2 + 2

"""


class MinHeap:
    def __init__(self, array: 'list[int]') -> None:
        self.heap = self.build_heap(array)

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
            if child_two_idx != -1 and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
            
            # The child that have to be swapped is 
            # less than the current number that is checked, swap it.
            if heap[idx_to_swap] < heap[current_idx]:
                self.swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return
    
    def sift_up(self, current_idx, heap):
        parent_idx = (current_idx - 1) // 2
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            self.swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = (current_idx - 1) // 2

    def peek(self):
        return self.heap[0]
    
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove

    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)
    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
   

def main() -> None:
    array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    MH = MinHeap(array)
    MH.build_heap(array)
    
    MH.insert(76)
    assert MH.heap == [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
    
    MH.remove()
    assert MH.heap == [2, 7, 6, 24, 8, 8, 24, 391, 76, 56, 12, 24, 48, 41]
    
    MH.remove()
    assert MH.heap == [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48]


if __name__ == '__main__':
    main()
