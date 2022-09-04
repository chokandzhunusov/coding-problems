"""
Time complexity: 
    O(k^n) for first 2 solutions
        n => the height of staircases
        k => max steps allowed
    O(n) for solution 3 with window slicing
Space complexity: O(n)
"""


# Solution 1
def number_of_ways_to_top(height: 'int', max_steps: 'int'):
    if height <= 1:
        return 1
    
    number_of_ways = 0
    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top(height - step, max_steps)
    
    return number_of_ways


def staircase_traversal_recur(height: 'int', max_steps: 'int'):
    return number_of_ways_to_top(height, max_steps)


# Solution 2
def number_of_ways_to_top_memoized(height: 'int', max_steps: 'int', memo: 'dict'):
    if height in memo:
        return memo[height]
    
    number_of_ways = 0
    for step in range(1, min(max_steps, height) + 1):
        number_of_ways += number_of_ways_to_top_memoized(height - step, max_steps, memo)
    
    memo[height] = number_of_ways
    
    return number_of_ways


def staircase_traversal_memoized(height: 'int', max_steps: 'int'):
    return number_of_ways_to_top_memoized(height, max_steps, {0: 1, 1: 1})


# Solution 3
def staircase_traversal_iter(height: 'int', max_steps: 'int'):
    current_number_of_ways = 0
    ways_to_top = [1]

    for current_height in range(1, height + 1):
        start_of_window = current_height - max_steps - 1
        end_of_window = current_height - 1
    
        if start_of_window >= 0:
            current_number_of_ways -= ways_to_top[start_of_window]
    
        current_number_of_ways += ways_to_top[end_of_window]
        ways_to_top.append(current_number_of_ways)
    
    return ways_to_top[height]


def main() -> None:
    height = 4
    max_steps = 2
    assert staircase_traversal_iter(height, max_steps) == 5
    assert staircase_traversal_recur(height, max_steps) == 5
    assert staircase_traversal_iter(height, max_steps) == 5


if __name__ == '__main__':
    main()
