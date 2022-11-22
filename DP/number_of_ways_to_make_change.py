"""
Time complexity: O(nd)
Space complexity: O(n)
"""

def number_of_ways_to_make_change(n, denoms):
    ways = [0 for amount in range(n+1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n]


def main() -> None:
    denoms = [1, 5]
    print(number_of_ways_to_make_change(10, denoms))
    return


if __name__ == '__main__':
    main()
