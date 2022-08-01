"""
Time complexity: O(nlogn)
Space complexity: O(n)
"""
    

def merge_overlapping_intervals(intervals: 'list[list[int]]') -> 'list[list[int]]':
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged_intervals = []
    current_interval = sorted_intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in sorted_intervals:
        _, end_of_current_interval = current_interval
        start_of_next_interval, end_of_next_interval = next_interval

        if end_of_current_interval >= start_of_next_interval:
            current_interval[1] = max(end_of_current_interval, end_of_next_interval)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)
    
    return merged_intervals


def main() -> None:
    ans = merge_overlapping_intervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
