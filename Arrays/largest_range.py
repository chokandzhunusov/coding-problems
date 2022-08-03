"""
Time complexity: O(n)
Space complexity: O(n)
"""


def largest_range(array: 'list[int]') -> 'list[int]':
    best_range = []
    longest_len = 0
    nums = {}

    for num in array:
        nums[num] = True

    for num in array:
        if not nums[num]:
            continue
            
        nums[num] = False
        current_len = 1
        left = num - 1
        right = num + 1

        while left in nums:
            nums[left] = False
            current_len += 1
            left -= 1

        while right in nums:
            nums[right] = False
            current_len += 1
            right += 1

        if current_len > longest_len:
            longest_len = current_len
            best_range = [left+1, right-1]
    return best_range


def main() -> None:
    # ans = largest_range([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6])
    ans = largest_range([4, 2, 1, 3])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
