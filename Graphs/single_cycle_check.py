"""
Time complexity: O(n)
Space complexity: O(1)
"""


def get_next_index(current_index: 'int', array: 'list[int]'):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    return next_index if next_index >= 0 else next_index + len(array)
    

def has_single_cycle(array: 'list[int]'):
    current_index = 0
    num_nodes_visited = 0

    while num_nodes_visited < len(array):
        if num_nodes_visited > 0 and current_index == 0:
            return False
        num_nodes_visited += 1
        current_index = get_next_index(current_index, array)
    return current_index == 0
            

def main() -> None:
    # ans = has_single_cycle([2, 3, 1, -4, -4, 2]) 
    ans = has_single_cycle([2, 2, -1]) 
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
