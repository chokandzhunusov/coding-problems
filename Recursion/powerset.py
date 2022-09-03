"""
Time complexity: O(2^n * n) 
    2^n => At every element we doubling the number of subsets
    n => each of those elements has at least n/2 elements at average
Space complexity: O(2^n * n)
"""


def get_powersets_recursive(array: 'list[int]', idx=None):
    if idx is None:
        idx = len(array) - 1
    
    if idx < 0:
        return [[]]
    
    element = array[idx]
    subsets = get_powersets_recursive(array, idx-1)
    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [element])
    return subsets
    

def get_powersets_iterative(array: 'list[int]'):
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            subsets.append([element] + subsets[i])
    return subsets


def main() -> None:
    array = [1, 2, 3]
    assert get_powersets_recursive(array) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert get_powersets_iterative(array) == [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
    


if __name__ == '__main__':
    main()
