"""
Time complexity: O(nlog(k)) n => number of elements in array, k => how far is given shift
Space complexity: O(k)
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

    def is_empty(self):
        return len(self.heap) == 0
    
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
   

def sort_k_sorted_array(array: 'list[int]', k: 'int'):
    min_heap_with_k_sorted_elements = MinHeap(array[:min(k+1, len(array))])

    next_index_to_insert_element = 0
    for idx in range(k+1, len(array)):
        min_element = min_heap_with_k_sorted_elements.remove()
        array[next_index_to_insert_element] = min_element
        next_index_to_insert_element += 1

        current_element = array[idx]
        min_heap_with_k_sorted_elements.insert(current_element)

    while not min_heap_with_k_sorted_elements.is_empty():
        min_element = min_heap_with_k_sorted_elements.remove()
        array[next_index_to_insert_element] = min_element
        next_index_to_insert_element += 1
    
    return array


def main() -> None:
    array = [3, 2, 1, 5, 4, 7, 6, 5]
    sort_k_sorted_array(array, 3)
    assert [1, 2, 3, 4, 5, 5, 6, 7] == array
    

if __name__ == '__main__':
    main()
