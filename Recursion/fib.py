"""
Time complexity: 
    fib_recur O(2^n)
    fib_recur_with_memo O(n)
    fib_iter O(n)

Space complexity: O()
    fib_recur O(n)
    fib_recur_with_memo O(n)
    fib_iter O(1)
"""


def fib_recur(n):
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1
    
    return fib_recur(n - 1) + fib_recur(n - 2)


def fib_recur_with_memo(n, memo={1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_recur_with_memo(n - 1, memo) + fib_recur_with_memo(n - 2, memo)
        return memo[n]


def fib_iter(n):
    last_two_nums = [0, 1]
    counter = 3  # to calculate starting from third fib num
    while counter <= n:
        next_fib_num = last_two_nums[0] + last_two_nums[1]
        last_two_nums[0] = last_two_nums[1]
        last_two_nums[1] = next_fib_num
        counter += 1
    return last_two_nums[1] if n > 1 else last_two_nums[0]


def main() -> None:
    assert fib_recur(5) == 3
    assert fib_recur_with_memo(7) == 8
    assert fib_iter(17) == 987
    

if __name__ == '__main__':
    main()
