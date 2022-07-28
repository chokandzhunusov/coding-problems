"""
Time complexity: O(nlogn) for sorting, we removed n of actuall loop at L11
Space complexity: O(1) bcs of sorted coins
"""


def non_constructible_change(coins: "list[int]") -> "int":
    coins.sort()
    change = 0
    
    for c in coins:
        if change + 1 < c:
            return change + 1
        change += c

    return change + 1


def main() -> None:
    ans = non_constructible_change([5, 7, 1, 1, 2, 3, 22])
    print(f'The answer is: {ans}')


if __name__ == '__main__':
    main()
