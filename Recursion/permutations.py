"""
Time complexity: O(n*n)
Space complexity: O(n*n!)
"""


def swap(array: 'list[int]', i: 'int', j: 'int'):
    array[i], array[j] = array[j], array[i]


def helper(i: 'int', array: 'list[int]', permutations: 'list'):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            helper(i+1, array, permutations)
            swap(array, i, j)
    

def get_permutations(array: 'list[any]'):
    permutations = []
    helper(0, array, permutations)
    return permutations


def main() -> None:
    array = [1, 2, 3]
    assert get_permutations(array) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


if __name__ == '__main__':
    main()
